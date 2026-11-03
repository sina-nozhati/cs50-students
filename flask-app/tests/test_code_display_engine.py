"""تست‌های جامع مهندسی سیستم نمایش کد و واکنش‌گرایی (Code Display & Responsive UI Engineering)."""
import html as html_lib
import re
from pathlib import Path
from app.content.md_render import render_markdown


def test_code_engine_assets_exist_and_valid():
    """بررسی وجود فایل جاوااسکریپت موتور کد و سینتکس صحیح."""
    js_path = Path("static/js/code-engine.js")
    assert js_path.exists(), "فایل code-engine.js در مسیر static/js موجود نیست"
    
    js_content = js_path.read_text(encoding="utf-8")
    assert "enhanceCodeBlock" in js_content
    assert "detectLanguage" in js_content
    assert "copyTextToClipboard" in js_content
    assert "wrap-mode" in js_content
    assert "is-collapsible" in js_content
    assert "htmx:afterSwap" in js_content


def test_design_tokens_contain_code_system_rules():
    """بررسی تعریف استایل‌های جامع و واکنش‌گرای کد در _design-tokens.html."""
    tokens_path = Path("templates/_partials/_design-tokens.html")
    assert tokens_path.exists()
    content = tokens_path.read_text(encoding="utf-8")
    
    # الزامات کدهای تک‌خطی (Inline Code)
    assert "white-space: break-spaces" in content
    assert "word-break: break-word" in content
    assert "overflow-wrap: break-word" in content
    assert "direction: ltr !important" in content
    
    # الزامات فریم و بلوک‌های کد (Block Code)
    assert ".code-block-wrapper" in content
    assert ".code-block-header" in content
    assert ".code-line-numbers" in content
    assert ".code-block-viewport" in content
    assert ".wrap-mode" in content
    assert ".is-collapsible" in content
    assert ".code-expand-drawer" in content
    assert "overscroll-behavior-x: contain" in content


def test_base_templates_include_code_engine():
    """بررسی بارگذاری code-engine.js در base.html و admin_base.html."""
    base_html = Path("templates/base.html").read_text(encoding="utf-8")
    assert "code-engine.js" in base_html, "code-engine.js در base.html بارگذاری نشده است"

    admin_base_html = Path("templates/admin/admin_base.html").read_text(encoding="utf-8")
    assert "code-engine.js" in admin_base_html, "code-engine.js در admin_base.html بارگذاری نشده است"


def test_single_line_ultra_long_code_rendering():
    """نمونه ۱: کد تک‌خطی بسیار طولانی (آدرس URL و دستور یکپارچه ۵۰۰ کاراکتری بدون فاصله)."""
    long_cmd = "curl -X POST https://api.cs50xanzali.ir/v1/auth/tokens/authenticate?client_id=cs50x_client_long_identifier_abcdef1234567890abcdef1234567890&redirect_uri=https://cs50xanzali.ir/callback&response_type=code&scope=read_kb_download_access_token_full_profile_diagnostics_analytics_leaderboard_progress_tracker_master_bundle_v1_v2&state=random_anti_csrf_token_xyz98765432109876543210"
    md = f"دستور احراز هویت به صورت زیر است:\n`{long_cmd}`"
    raw_html = render_markdown(md)
    unescaped = html_lib.unescape(raw_html)
    
    # محتوا نباید دچار تغییر یا برش شود و درون تگ code قرار گیرد
    assert long_cmd in unescaped
    assert "<code>" in raw_html


def test_multiline_whitespace_and_indentation_preservation():
    """نمونه ۲: کد چندخطی پایتون و C با تورفتگی‌های دقیق و معنادار."""
    python_code = (
        "def bubble_sort(numbers):\n"
        "    n = len(numbers)\n"
        "    for i in range(n):\n"
        "        for j in range(0, n - i - 1):\n"
        "            if numbers[j] > numbers[j + 1]:\n"
        "                # Swap numbers in-place\n"
        "                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]\n"
        "    return numbers"
    )
    md = f"```python\n{python_code}\n```"
    raw_html = render_markdown(md)
    unescaped = html_lib.unescape(raw_html)
    
    # ساختار خطوط و تورفتگی‌ها کاملاً دست‌نخورده باقی می‌ماند
    assert "def bubble_sort" in unescaped
    assert "            if numbers[j] > numbers[j + 1]:" in unescaped
    assert "# Swap numbers in-place" in unescaped
    assert '<code class="language-python">' in raw_html


def test_multi_hundred_line_code_stability():
    """نمونه ۳: کد حجیم با بیش از ۳۰۰ خط برای اعتبارسنجی پایداری و بدون کرش رندرینگ."""
    lines = ["// CS50x Anzali Stress Test File - Header"]
    for i in range(1, 350):
        lines.append(f"int variable_item_{i:04d} = {i * 10}; // Definition line for index {i}")
    lines.append("// End of 350-line file")
    
    big_code = "\n".join(lines)
    md = f"```c\n{big_code}\n```"
    html = render_markdown(md)
    
    assert "variable_item_0001" in html
    assert "variable_item_0349" in html
    assert len(html.split("\n")) >= 350


def test_long_lines_inside_multiline_code():
    """نمونه ۴: خطوط طولانی داخل کد چندخطی (رشته‌های طویل و آرایه‌های بزرگ)."""
    code_with_long_lines = (
        "#include <stdio.h>\n"
        "int main(void) {\n"
        '    const char *long_banner = "==========================================================================================================================================================================";\n'
        '    const char *payload_data = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFsaSBOb3poYXRpIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";\n'
        '    printf("%s\\n%s\\n", long_banner, payload_data);\n'
        "    return 0;\n"
        "}"
    )
    md = f"```c\n{code_with_long_lines}\n```"
    html = render_markdown(md)
    
    assert "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" in html
    assert "======================================" in html


def test_json_structure_and_types():
    """نمونه ۵: سند JSON عمیق با مقادیر بولی، نال، اعداد اعشاری و رشته‌های فارسی و انگلیسی."""
    json_code = (
        '{\n'
        '  "status": "success",\n'
        '  "code": 200,\n'
        '  "data": {\n'
        '    "course": "CS50x Anzali",\n'
        '    "is_active": true,\n'
        '    "deleted_at": null,\n'
        '    "student_count": 48,\n'
        '    "average_score": 94.75,\n'
        '    "modules": ["Week 0 Scratch", "Week 1 C", "Week 2 Arrays", "Week 7 SQL"]\n'
        '  }\n'
        '}'
    )
    md = f"```json\n{json_code}\n```"
    raw_html = render_markdown(md)
    unescaped = html_lib.unescape(raw_html)
    
    assert '"status": "success"' in unescaped
    assert '"is_active": true' in unescaped
    assert '"deleted_at": null' in unescaped
    assert '<code class="language-json">' in raw_html


def test_complex_sql_query_rendering():
    """نمونه ۶: کوئری پیچیده SQL با چند JOIN، شرایط WHERE و مقادیر رشته‌ای."""
    sql_code = (
        "SELECT students.id, students.full_name, COUNT(submissions.id) AS total_submissions,\n"
        "       COALESCE(SUM(submissions.score), 0) AS cumulative_score\n"
        "FROM users students\n"
        "INNER JOIN cohorts ON students.cohort_id = cohorts.id\n"
        "LEFT JOIN submissions ON submissions.user_id = students.id AND submissions.status = 'approved'\n"
        "WHERE cohorts.code = 'CS50X-ANZALI-2026'\n"
        "  AND students.role = 'student'\n"
        "GROUP BY students.id, students.full_name\n"
        "HAVING COUNT(submissions.id) >= 5\n"
        "ORDER BY cumulative_score DESC\n"
        "LIMIT 10 OFFSET 0;"
    )
    md = f"```sql\n{sql_code}\n```"
    html = render_markdown(md)
    
    assert "SELECT students.id" in html
    assert "INNER JOIN cohorts" in html
    assert "CS50X-ANZALI-2026" in html
    assert '<code class="language-sql">' in html
