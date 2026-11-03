/**
 * CS50x Anzali — Professional Code Display & Responsive UI Engineering Engine
 * 
 * Features:
 *  1. Automatic wrapping into macOS-style dark terminal frame.
 *  2. Pure, uncorrupted clipboard copy (without line numbers or UI elements).
 *  3. Soft-wrap toggle (switches between horizontal scroll and responsive soft wrap).
 *  4. Intelligent line numbering (non-selectable, aligned gutter).
 *  5. Height control & Expand/Collapse for multi-hundred-line code blocks.
 *  6. Non-destructive syntax highlighting for C, Python, SQL, JSON, Bash, HTML/CSS.
 *  7. Full reactivity: handles HTMX swaps and dynamically loaded content.
 *  8. Mobile-native touch targets and overscroll isolation.
 */

(function () {
  'use strict';

  // زبان‌ها و کلمات کلیدی استاندارد
  const KEYWORDS = {
    c: new Set([
      'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
      'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
      'inline', 'int', 'long', 'register', 'restrict', 'return', 'short',
      'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union',
      'unsigned', 'void', 'volatile', 'while', 'bool', 'string', 'size_t',
      'NULL', 'true', 'false', '#include', '#define', '#ifdef', '#ifndef', '#endif'
    ]),
    python: new Set([
      'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
      'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from',
      'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
      'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield',
      'True', 'False', 'None', 'self', 'int', 'str', 'float', 'list', 'dict', 'set'
    ]),
    sql: new Set([
      'SELECT', 'FROM', 'WHERE', 'INSERT', 'INTO', 'UPDATE', 'DELETE', 'JOIN',
      'INNER', 'LEFT', 'RIGHT', 'FULL', 'OUTER', 'ON', 'GROUP', 'BY', 'ORDER',
      'HAVING', 'LIMIT', 'OFFSET', 'CREATE', 'TABLE', 'DROP', 'ALTER', 'PRIMARY',
      'KEY', 'FOREIGN', 'REFERENCES', 'NOT', 'NULL', 'DEFAULT', 'UNIQUE', 'CHECK',
      'INDEX', 'VIEW', 'AND', 'OR', 'IN', 'IS', 'LIKE', 'BETWEEN', 'AS', 'COUNT',
      'SUM', 'AVG', 'MIN', 'MAX', 'DISTINCT', 'UNION', 'ALL', 'CASE', 'WHEN',
      'THEN', 'ELSE', 'END', 'INTEGER', 'TEXT', 'REAL', 'BLOB', 'VARCHAR', 'BOOLEAN'
    ]),
    bash: new Set([
      'echo', 'cd', 'ls', 'pwd', 'mkdir', 'rm', 'cp', 'mv', 'touch', 'cat',
      'grep', 'find', 'chmod', 'chown', 'sudo', 'apt', 'curl', 'wget', 'git',
      'make', 'check50', 'style50', 'help50', 'submit50', 'python', 'python3',
      'pip', 'export', 'source', 'if', 'then', 'else', 'elif', 'fi', 'for',
      'while', 'do', 'done', 'case', 'esac', 'function', 'return', 'exit'
    ])
  };

  /**
   * فرار امن کاراکترهای HTML
   */
  function escapeHtml(str) {
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  /**
   * تشخیص هوشمند زبان قطعه‌کد از کلاس یا محتوا
   */
  function detectLanguage(codeEl, rawText) {
    // ۱. بررسی کلاس‌های تگ code و والد
    const classList = (codeEl.className || '') + ' ' + (codeEl.parentElement.className || '');
    const langMatch = classList.match(/language-([a-zA-Z0-9_\+#]+)/i) || classList.match(/lang-([a-zA-Z0-9_\+#]+)/i);
    if (langMatch) {
      const l = langMatch[1].toLowerCase();
      if (l === 'c' || l === 'cpp' || l === 'h') return 'C';
      if (l === 'py' || l === 'python') return 'PYTHON';
      if (l === 'sql' || l === 'sqlite') return 'SQL';
      if (l === 'json') return 'JSON';
      if (l === 'sh' || l === 'bash' || l === 'shell' || l === 'zsh') return 'BASH';
      if (l === 'html' || l === 'xml') return 'HTML';
      if (l === 'css') return 'CSS';
      if (l === 'js' || l === 'javascript' || l === 'ts') return 'JAVASCRIPT';
      return l.toUpperCase();
    }

    // ۲. بررسی ویژگی data-lang
    const dataLang = codeEl.getAttribute('data-lang') || codeEl.parentElement.getAttribute('data-lang');
    if (dataLang) return dataLang.toUpperCase();

    // ۳. حدس ساختاری بر اساس نشانه‌های کد
    const trimmed = rawText.trim();
    if (trimmed.startsWith('{') && trimmed.endsWith('}') && (trimmed.includes('":') || trimmed.includes('",'))) return 'JSON';
    if (trimmed.startsWith('[') && trimmed.endsWith(']') && trimmed.includes('{')) return 'JSON';
    if (/^\s*(#include|int\s+main|printf\s*\(|void\s+\w+\()/m.test(trimmed)) return 'C';
    if (/^\s*(def\s+\w+|import\s+\w+|from\s+\w+\s+import|print\s*\()/m.test(trimmed)) return 'PYTHON';
    if (/^\s*(SELECT|INSERT\s+INTO|CREATE\s+TABLE|UPDATE\s+\w+\s+SET)\b/im.test(trimmed)) return 'SQL';
    if (/^\s*(\$|\b(sudo|curl|wget|make|check50|apt-get|git\s+))\b/m.test(trimmed)) return 'BASH';

    return 'CODE';
  }

  /**
   * هایلایت غیرمخرب و بدون تغییر کاراکترهای اصلی
   */
  function highlightSyntax(rawCode, lang) {
    if (!rawCode) return '';
    const l = lang.toLowerCase();

    // هایلایت اختصاصی JSON
    if (l === 'json') {
      try {
        // برای JSON معتبر با فرمت تمیز
        const regex = /("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g;
        return escapeHtml(rawCode).replace(regex, function (match) {
          let cls = 'token-num';
          if (/^"/.test(match)) {
            if (/:$/.test(match)) {
              cls = 'token-kw'; // کلید JSON
            } else {
              cls = 'token-str'; // مقدار رشته‌ای
            }
          } else if (/true|false/.test(match)) {
            cls = 'token-con';
          } else if (/null/.test(match)) {
            cls = 'token-typ';
          }
          return '<span class="' + cls + '">' + match + '</span>';
        });
      } catch (e) {
        return escapeHtml(rawCode);
      }
    }

    // هایلایت لکسیکال C, Python, SQL, Bash
    let html = escapeHtml(rawCode);

    // ۱. کامنت‌های چندخطی /* ... */
    html = html.replace(/(\/\*[\s\S]*?\*\/)/g, '<span class="token-com">$1</span>');

    // ۲. کامنت‌های تک‌خطی (// در C، # در پایتون/بش، -- در SQL)
    if (l === 'c' || l === 'javascript' || l === 'cpp') {
      html = html.replace(/(\/\/[^\n]*)/g, '<span class="token-com">$1</span>');
    } else if (l === 'python' || l === 'bash') {
      html = html.replace(/(#[^\n]*)/g, '<span class="token-com">$1</span>');
    } else if (l === 'sql') {
      html = html.replace(/(--[^\n]*)/g, '<span class="token-com">$1</span>');
    }

    // ۳. رشته‌ها "..." و '...'
    html = html.replace(/(".*?"|'.*?'|`.*?`)/g, '<span class="token-str">$1</span>');

    // ۴. اعداد
    html = html.replace(/\b(\d+(?:\.\d+)?(?:[eE][+-]?\d+)?|0x[0-9a-fA-F]+)\b/g, '<span class="token-num">$1</span>');

    // ۵. کلمات کلیدی مرتبط با زبان
    const kwSet = KEYWORDS[l] || KEYWORDS.c;
    const kwRegex = new RegExp('\\b(' + Array.from(kwSet).map(k => k.replace(/[#]/g, '\\#')).join('|') + ')\\b', l === 'sql' ? 'gi' : 'g');
    html = html.replace(kwRegex, function (match) {
      return '<span class="token-kw">' + match + '</span>';
    });

    // ۶. فراخوانی توابع (e.g. printf, get_int)
    html = html.replace(/\b([a-zA-Z_]\w*)\s*(?=\()/g, '<span class="token-fn">$1</span>');

    return html;
  }

  /**
   * کپی امن و بدون دست‌کاری محتوا در کلیپ‌بورد با فال‌بک
   */
  function copyTextToClipboard(text, onSuccess, onError) {
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(onSuccess).catch(function () {
        fallbackCopyText(text, onSuccess, onError);
      });
    } else {
      fallbackCopyText(text, onSuccess, onError);
    }
  }

  function fallbackCopyText(text, onSuccess, onError) {
    try {
      const textArea = document.createElement('textarea');
      textArea.value = text;
      textArea.style.position = 'fixed';
      textArea.style.top = '-9999px';
      textArea.style.left = '-9999px';
      textArea.setAttribute('readonly', '');
      document.body.appendChild(textArea);
      textArea.select();
      const success = document.execCommand('copy');
      document.body.removeChild(textArea);
      if (success) onSuccess();
      else if (onError) onError();
    } catch (e) {
      if (onError) onError();
    }
  }

  /**
   * پردازش و ارتقای یک بلوک کد منفرد
   */
  function enhanceCodeBlock(preEl) {
    if (!preEl || preEl.getAttribute('data-code-enhanced') === 'true') return;
    
    // اگر از قبل داخل code-block-wrapper است، رد شو
    if (preEl.closest('.code-block-wrapper')) {
      preEl.setAttribute('data-code-enhanced', 'true');
      return;
    }

    const codeEl = preEl.querySelector('code') || preEl;
    const rawText = codeEl.textContent || '';
    if (!rawText.trim()) return;

    // ثبت به عنوان پردازش‌شده
    preEl.setAttribute('data-code-enhanced', 'true');

    // تعیین زبان و ساختار خطوط
    const lang = detectLanguage(codeEl, rawText);
    const lines = rawText.replace(/\r\n/g, '\n').replace(/\r/g, '\n').split('\n');
    // اگر آخرین خط خالی است، آن را حذف نکنیم تا فرمت اصلی حفظ شود
    const lineCount = lines.length;

    // ایجاد فریم macOS
    const wrapper = document.createElement('div');
    wrapper.className = 'code-block-wrapper font-mono';
    wrapper.setAttribute('dir', 'ltr');

    // ۱. هدر بلوک کد
    const header = document.createElement('div');
    header.className = 'code-block-header';

    // سمت چپ: دکمه‌های ۳ رنگ macOS
    const dots = document.createElement('div');
    dots.className = 'traffic-dots';
    dots.innerHTML = '<span class="traffic-dot dot-red"></span><span class="traffic-dot dot-yellow"></span><span class="traffic-dot dot-green"></span>';

    // وسط: بج نام زبان و تعداد خطوط
    const info = document.createElement('div');
    info.className = 'code-info-pill';
    info.innerHTML = '<span class="code-lang-tag">' + escapeHtml(lang) + '</span>' +
                     (lineCount > 1 ? '<span class="code-lines-count num">' + lineCount + ' lines</span>' : '');

    // سمت راست: اکشن‌ها (Wrap + Copy)
    const actions = document.createElement('div');
    actions.className = 'code-actions';

    // دکمه شکستن خطوط (Wrap Toggle)
    const wrapBtn = document.createElement('button');
    wrapBtn.type = 'button';
    wrapBtn.className = 'code-action-btn wrap-btn';
    wrapBtn.setAttribute('title', 'تغییر وضعیت شکستن خطوط (Soft Wrap)');
    wrapBtn.setAttribute('aria-label', 'شکستن خودکار خطوط');
    wrapBtn.innerHTML = '<svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M3 10h14a4 4 0 010 8h-3m0 0l3-3m-3 3l3 3M3 6h18M3 14h7M3 18h7"/></svg><span>Wrap</span>';

    wrapBtn.addEventListener('click', function (e) {
      e.preventDefault();
      wrapper.classList.toggle('wrap-mode');
      const isWrapped = wrapper.classList.contains('wrap-mode');
      wrapBtn.classList.toggle('active', isWrapped);
      wrapBtn.querySelector('span').textContent = isWrapped ? 'Unwrap' : 'Wrap';
    });

    // دکمه کپی کد (Copy Button)
    const copyBtn = document.createElement('button');
    copyBtn.type = 'button';
    copyBtn.className = 'code-action-btn copy-btn';
    copyBtn.setAttribute('title', 'کپی کد تمیز');
    copyBtn.setAttribute('aria-label', 'کپی کد در کلیپ‌بورد');
    copyBtn.innerHTML = '<svg class="w-3.5 h-3.5 copy-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg><span class="copy-label">کپی</span>';

    copyBtn.addEventListener('click', function (e) {
      e.preventDefault();
      copyTextToClipboard(rawText, function () {
        copyBtn.classList.add('copied');
        copyBtn.innerHTML = '<svg class="w-3.5 h-3.5 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg><span class="text-emerald-400 font-bold">کپی شد!</span>';
        setTimeout(function () {
          copyBtn.classList.remove('copied');
          copyBtn.innerHTML = '<svg class="w-3.5 h-3.5 copy-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg><span class="copy-label">کپی</span>';
        }, 2000);
      }, function () {
        alert('امکان کپی خودکار فراهم نشد. لطفاً کد را دستی کپی فرمایید.');
      });
    });

    actions.appendChild(wrapBtn);
    actions.appendChild(copyBtn);

    header.appendChild(dots);
    header.appendChild(info);
    header.appendChild(actions);

    // ۲. ویوپورت اسکرول و نمایش کد
    const viewport = document.createElement('div');
    viewport.className = 'code-block-viewport custom-scrollbar';

    // ناودان شماره خطوط (فقط برای بیش از ۱ خط)
    if (lineCount > 1) {
      const gutter = document.createElement('div');
      gutter.className = 'code-line-numbers select-none';
      gutter.setAttribute('aria-hidden', 'true');
      let gutterHtml = '';
      for (let i = 1; i <= lineCount; i++) {
        gutterHtml += '<span>' + i + '</span>\n';
      }
      gutter.innerHTML = gutterHtml;
      viewport.appendChild(gutter);
    }

    // بدنه کد با هایلایت ایمن (اگر از قبل اسپن‌های هایلایت ندارد)
    const newPre = document.createElement('pre');
    newPre.className = 'code-content custom-scrollbar';
    newPre.setAttribute('dir', 'ltr');

    const newCode = document.createElement('code');
    newCode.className = codeEl.className || ('language-' + lang.toLowerCase());
    newCode.setAttribute('dir', 'ltr');

    // اگر کد قبلاً اسپن‌های استایل دارد از innerHTML استفاده می‌کنیم، در غیر این‌صورت با هایلایتر داخلی فرمت می‌کنیم
    if (codeEl.querySelector('span')) {
      newCode.innerHTML = codeEl.innerHTML;
    } else {
      newCode.innerHTML = highlightSyntax(rawText, lang);
    }

    newPre.appendChild(newCode);
    viewport.appendChild(newPre);

    wrapper.appendChild(header);
    wrapper.appendChild(viewport);

    // ۳. مدیریت بلوک‌های کد طولانی (Expand / Collapse)
    const COLLAPSE_THRESHOLD_LINES = 22;
    if (lineCount > COLLAPSE_THRESHOLD_LINES) {
      wrapper.classList.add('is-collapsible');

      const drawer = document.createElement('div');
      drawer.className = 'code-expand-drawer';

      const expandBtn = document.createElement('button');
      expandBtn.type = 'button';
      expandBtn.className = 'code-expand-btn';
      expandBtn.innerHTML = '<span>نمایش تمام کد (' + lineCount + ' خط)</span><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>';

      expandBtn.addEventListener('click', function (e) {
        e.preventDefault();
        const isExp = wrapper.classList.toggle('is-expanded');
        if (isExp) {
          expandBtn.innerHTML = '<span>جمع کردن کد</span><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 15l7-7 7 7"/></svg>';
        } else {
          expandBtn.innerHTML = '<span>نمایش تمام کد (' + lineCount + ' خط)</span><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>';
          // اسکرول نرم به ابتدای بلوک کد
          wrapper.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      });

      drawer.appendChild(expandBtn);
      wrapper.appendChild(drawer);
    }

    // جایگزینی تمیز در DOM
    preEl.parentNode.replaceChild(wrapper, preEl);
  }

  /**
   * اسکن و ارتقای کلیه بلوک‌های کد در صفحه
   */
  function initCodeEngine(root) {
    const context = root || document;
    // یافتن تمام تگ‌های pre در بخش‌های محتوایی (kb-prose، مقالات، کارت‌ها)
    const pres = context.querySelectorAll('.kb-prose pre, article pre, .card-harvard pre, pre:not(.no-enhance)');
    pres.forEach(function (p) {
      // رد کردن ملوانی mermaid که هندلر جداگانه دارند
      if (p.classList.contains('kb-mermaid-code') || p.querySelector('.mermaid')) return;
      enhanceCodeBlock(p);
    });
  }

  // اجرای اولیه پس از بارگذاری DOM
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initCodeEngine();
    });
  } else {
    initCodeEngine();
  }

  // اجرای مجدد روی سواپ‌های HTMX برای المان‌های پویا
  document.addEventListener('htmx:afterSwap', function (evt) {
    if (evt.detail && evt.detail.target) {
      initCodeEngine(evt.detail.target);
    } else {
      initCodeEngine();
    }
  });

  // افشای سراسری برای فراخوانی در کامپوننت‌های SPA / Alpine
  window.CS50CodeEngine = {
    init: initCodeEngine,
    enhance: enhanceCodeBlock
  };

})();
