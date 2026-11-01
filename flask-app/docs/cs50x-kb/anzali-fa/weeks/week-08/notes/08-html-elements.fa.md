---
id: w08-n08
type: note
title: 'فهرست، جدول، تصویر، ویدئو و پیوند (HTML: Lists, Tables, Media and Links)'
title_fa: فهرست، جدول، تصویر، ویدئو و پیوند
title_en: 'HTML: Lists, Tables, Media and Links'
week: 8
parent: w08-fa
lang: fa
source_type: translated-rewritten
origin: translated-rewritten
official_section: HTML
official_anchor: html
source_url: https://cs50.harvard.edu/x/2026/notes/8/#html
source_refs:
- src-notes-8#html
- src-transcript-8
- src-html-spec
- src-web-box-8
- src-anzali-authored-8
- src-srt-8
concept_ids:
- w08-c-lists
- w08-c-table
- w08-c-img-alt
- w08-c-video
- w08-c-anchor-link
- w08-c-void-elements
prev: w08-n07
next: w08-n09
order: 8
video:
  youtube_id: yYst7puZXjw
  start: '59:49'
  start_seconds: 3589
  url: https://www.youtube.com/watch?v=yYst7puZXjw&t=3589s
  origin: inference
  basis: first lecture8.srt cue (after the previous note's cue) containing the phrase "the tag I'll use first is going to be UL"
license: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
attribution: Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.
retrieved_at: '2026-10-18T05:10:41+03:30'
verified_at: '2026-10-29T07:44:55+03:30'
review_status: draft-needs-human-review
content_policy: Faithful Persian rewrite; HTML, CSS and command code copied exactly from the official notes (fence language html, css, bash or text); results marked «اجراشده روی جعبهٔ ساخت» were run with Node and jsdom (and html5lib/tinycss2 for markup) on the build box; authored material is marked تألیفی and contains no Persian inside code; transcript-only facts are marked «از سخنرانی», section facts «از جلسهٔ حل تمرین», shorts facts «از ویدئوی کوتاه». Callouts use GitHub-style markers ([!NOTE], [!TIP], [!IMPORTANT], [!WARNING]) followed by a bold Persian label line so they degrade to a labelled blockquote in the current renderer.
---

# فهرست، جدول، تصویر، ویدئو و پیوند

> **منبع رسمی:** بخش «HTML» از [درس‌نامهٔ هفتهٔ ۸ CS50x 2026](https://cs50.harvard.edu/x/2026/notes/8/#html). این صفحه بازنویسی وفادار فارسی است، نه ترجمهٔ کلمه‌به‌کلمه. کدها عیناً از منبع آمده‌اند؛ مطالب **تألیفی** و نکته‌های **از سخنرانی** جدا برچسب خورده‌اند.

> **ویدئوی سخنرانی:** [از دقیقهٔ ۵۹:۴۹ تا حدود ۱:۱۵:۴۹](https://www.youtube.com/watch?v=yYst7puZXjw&t=3589s). زمان شروع از زیرنویس رسمی استخراج شده و مرز بخش‌ها استنتاج ویراستاری است.

## چرا این بخش مهم است

با یک `hello` فقط نمی‌شود صفحه ساخت. پاراگراف، عنوان، فهرست، جدول، تصویر، ویدئو و پیوند قطعه‌هایی‌اند که تقریباً هر صفحه‌ای، از جمله صفحهٔ خانگی مجموعه‌تمرین این هفته، با آن‌ها ساخته می‌شود.

## پاراگراف‌ها

- چون فاصله‌ها و تورفتگی در HTML عملاً نادیده گرفته می‌شوند، باید برای باز و بسته کردن پاراگراف از برچسب `<p>` استفاده کنی:

```html
<!DOCTYPE html>

<!-- Demonstrates paragraphs -->

<html lang="en">
    <head>
        <title>paragraphs</title>
    </head>
    <body>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis scelerisque quam, vel hendrerit lectus viverra eu. Praesent posuere eget lectus ut faucibus. Etiam eu velit laoreet, gravida lorem in, viverra est. Cras ut purus neque. In porttitor non lorem id lobortis. Mauris gravida metus libero, quis maximus dui porta at. Donec lacinia felis consectetur venenatis scelerisque. Nulla eu nisl sollicitudin, varius velit sit amet, vehicula erat. Curabitur sollicitudin felis sit amet orci mattis, a tempus nulla pulvinar. Aliquam erat volutpat.
        </p>
        <p>
            Mauris ut dui in eros semper hendrerit. Morbi vel elit mi. Sed sit amet ex non quam dignissim dignissim et vel arcu. Pellentesque eget elementum orci. Morbi ac cursus ex. Pellentesque quis turpis blandit orci dapibus semper sed non nunc. Nulla et dolor nec lacus finibus volutpat. Sed non lorem diam. Donec feugiat interdum interdum. Vivamus et justo in enim blandit fermentum vel at elit. Phasellus eu ante vitae ligula varius aliquet. Etiam id posuere nibh.
        </p>
        <p>
            Aenean venenatis convallis ante a rhoncus. Nullam in metus vel diam vehicula tincidunt. Donec lacinia metus sem, sit amet egestas elit blandit sit amet. Nunc egestas sem quis nisl mattis semper. Pellentesque ut magna congue lorem eleifend sodales. Donec tortor tortor, aliquam vitae mollis sed, interdum ut lectus. Mauris non purus quis ipsum lacinia tincidunt.
        </p>
        <p>
            Integer at justo lacinia libero blandit aliquam ut ut dui. Quisque tincidunt facilisis venenatis. Nullam dictum odio quis lorem luctus, vel malesuada dolor luctus. Aenean placerat faucibus enim a facilisis. Maecenas eleifend quis massa sed eleifend. Ut ultricies, dui ac vulputate hendrerit, ex metus iaculis diam, vitae fermentum libero dui et ante. Phasellus suscipit, arcu ut consequat sagittis, massa urna accumsan massa, eu aliquet nulla lorem vitae arcu. Pellentesque rutrum felis et metus porta semper. Nam ac consectetur mauris.
        </p>
        <p>
            Suspendisse rutrum vestibulum odio, sed venenatis purus condimentum sed. Morbi ornare tincidunt augue eu auctor. Vivamus sagittis ac lectus at aliquet. Nulla urna mauris, interdum non nibh in, vehicula porta enim. Donec et posuere sapien. Pellentesque ultrices scelerisque ipsum, vel fermentum nibh tincidunt et. Proin gravida porta ipsum nec scelerisque. Vestibulum fringilla erat at turpis laoreet, nec hendrerit nisi scelerisque.
        </p>
        <p>
            Sed quis malesuada mi. Nam id purus quis augue sagittis pharetra. Nulla facilisi. Maecenas vel fringilla ante. Cras tristique, arcu sit amet blandit auctor, urna elit ultricies lacus, a malesuada eros dui id massa. Aliquam sem odio, pretium vel cursus eget, scelerisque at urna. Vestibulum posuere a turpis consectetur consectetur. Cras consequat, risus quis tempor egestas, nulla ipsum ornare erat, nec accumsan nibh lorem nec risus. Integer at iaculis lacus. Integer congue nunc massa, quis molestie felis pellentesque vestibulum. Nulla odio tortor, aliquam nec quam in, ornare aliquet sapien.
        </p>
    </body>
</html>
```

- پاراگراف‌ها با `<p>` شروع و با `</p>` تمام می‌شوند.

> [!NOTE]
> **اجراشده روی جعبهٔ ساخت: فاصله‌ها فرو می‌ریزند**
> در jsdom، متن `<p>a    b\n   c</p>` در `innerHTML` همان‌طور با همهٔ فاصله‌ها ذخیره می‌شود؛ این مرورگر است که هنگام نمایش، هر رشته از فاصله و سطر جدید را به یک فاصله تبدیل می‌کند. پس سطر خالی در کد، پاراگراف تازه نمی‌سازد.

## عنوان‌ها

- HTML برای عنوان‌ها برچسب دارد:

```html
<!DOCTYPE html>

<!-- Demonstrates headings (for chapters, sections, subsections, etc.) -->

<html lang="en">

    <head>
        <title>headings</title>
    </head>

    <body>

        <h1>One</h1>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis scelerisque quam, vel hendrerit lectus viverra eu. Praesent posuere eget lectus ut faucibus. Etiam eu velit laoreet, gravida lorem in, viverra est. Cras ut purus neque. In porttitor non lorem id lobortis. Mauris gravida metus libero, quis maximus dui porta at. Donec lacinia felis consectetur venenatis scelerisque. Nulla eu nisl sollicitudin, varius velit sit amet, vehicula erat. Curabitur sollicitudin felis sit amet orci mattis, a tempus nulla pulvinar. Aliquam erat volutpat.
        </p>

        <h2>Two</h2>
        <p>
            Mauris ut dui in eros semper hendrerit. Morbi vel elit mi. Sed sit amet ex non quam dignissim dignissim et vel arcu. Pellentesque eget elementum orci. Morbi ac cursus ex. Pellentesque quis turpis blandit orci dapibus semper sed non nunc. Nulla et dolor nec lacus finibus volutpat. Sed non lorem diam. Donec feugiat interdum interdum. Vivamus et justo in enim blandit fermentum vel at elit. Phasellus eu ante vitae ligula varius aliquet. Etiam id posuere nibh.
        </p>

        <h3>Three</h3>
        <p>
            Aenean venenatis convallis ante a rhoncus. Nullam in metus vel diam vehicula tincidunt. Donec lacinia metus sem, sit amet egestas elit blandit sit amet. Nunc egestas sem quis nisl mattis semper. Pellentesque ut magna congue lorem eleifend sodales. Donec tortor tortor, aliquam vitae mollis sed, interdum ut lectus. Mauris non purus quis ipsum lacinia tincidunt.
        </p>

        <h4>Four</h4>
        <p>
            Integer at justo lacinia libero blandit aliquam ut ut dui. Quisque tincidunt facilisis venenatis. Nullam dictum odio quis lorem luctus, vel malesuada dolor luctus. Aenean placerat faucibus enim a facilisis. Maecenas eleifend quis massa sed eleifend. Ut ultricies, dui ac vulputate hendrerit, ex metus iaculis diam, vitae fermentum libero dui et ante. Phasellus suscipit, arcu ut consequat sagittis, massa urna accumsan massa, eu aliquet nulla lorem vitae arcu. Pellentesque rutrum felis et metus porta semper. Nam ac consectetur mauris.
        </p>

        <h5>Five</h5>
        <p>
            Suspendisse rutrum vestibulum odio, sed venenatis purus condimentum sed. Morbi ornare tincidunt augue eu auctor. Vivamus sagittis ac lectus at aliquet. Nulla urna mauris, interdum non nibh in, vehicula porta enim. Donec et posuere sapien. Pellentesque ultrices scelerisque ipsum, vel fermentum nibh tincidunt et. Proin gravida porta ipsum nec scelerisque. Vestibulum fringilla erat at turpis laoreet, nec hendrerit nisi scelerisque.
        </p>

        <h6>Six</h6>
        <p>
            Sed quis malesuada mi. Nam id purus quis augue sagittis pharetra. Nulla facilisi. Maecenas vel fringilla ante. Cras tristique, arcu sit amet blandit auctor, urna elit ultricies lacus, a malesuada eros dui id massa. Aliquam sem odio, pretium vel cursus eget, scelerisque at urna. Vestibulum posuere a turpis consectetur consectetur. Cras consequat, risus quis tempor egestas, nulla ipsum ornare erat, nec accumsan nibh lorem nec risus. Integer at iaculis lacus. Integer congue nunc massa, quis molestie felis pellentesque vestibulum. Nulla odio tortor, aliquam nec quam in, ornare aliquet sapien.
        </p>

    </body>

</html>
```

- `<h1>`، `<h2>` و `<h3>` سطح‌های مختلف عنوان را نشان می‌دهند.

> [!WARNING]
> **از ویدئوی کوتاه: بزرگی یا اهمیت؟ (d149)**
> ویدئوی HTML می‌گوید h1 تا h6 «کم‌کم بزرگ‌تر» می‌شوند؛ در واقع برعکس: `h1` مهم‌ترین و معمولاً بزرگ‌ترین است و `h6` کوچک‌ترین. اندازه هم فقط پیش‌فرض مرورگر است و با CSS عوض می‌شود؛ عدد سطح را برای ساختار انتخاب کن، نه برای اندازه.

## فهرست‌ها

- فهرست نامرتب:

```html
<!DOCTYPE html>

<!-- Demonstrates (unordered) lists -->

<html lang="en">
    <head>
        <title>list</title>
    </head>
    <body>
        <ul>
            <li>foo</li>
            <li>bar</li>
            <li>baz</li>
        </ul>
    </body>
</html>
```

- برچسب `<ul>` فهرستی **نامرتب** (`unordered list`) با سه مورد می‌سازد.
- فهرست مرتب:

```html
<!DOCTYPE html>

<!-- Demonstrates (ordered) lists -->

<html lang="en">
    <head>
        <title>list</title>
    </head>
    <body>
        <ol>
            <li>foo</li>
            <li>bar</li>
            <li>baz</li>
        </ol>
    </body>
</html>
```

- برچسب `<ol>` فهرستی **مرتب** (`ordered list`) با سه مورد می‌سازد؛ هر مورد با `<li>` می‌آید.

## جدول

```html
<!DOCTYPE html>

<!-- Demonstrates table -->

<html lang="en">
    <head>
        <title>table</title>
    </head>
    <body>
        <table>
            <tr>
                <td>1</td>
                <td>2</td>
                <td>3</td>
            </tr>
            <tr>
                <td>4</td>
                <td>5</td>
                <td>6</td>
            </tr>
            <tr>
                <td>7</td>
                <td>8</td>
                <td>9</td>
            </tr>
            <tr>
                <td>*</td>
                <td>0</td>
                <td>#</td>
            </tr>
        </table>
    </body>
</html>
```

- جدول‌ها هم برچسب‌هایی دارند که هر بخش را باز و بسته می‌کنند: `tr` یک سطر و `td` یک خانه. نحو **توضیح** (`comment`) در HTML را هم ببین: `<!-- ... -->`.

> [!TIP]
> **تألیفی: سرستون‌ها**
> این جدول صفحه‌کلید تلفن است و سرستون ندارد. برای جدولی با سرستون، HTML برچسب‌های `thead`، `tbody` و `th` را هم دارد؛ `th` خانه‌ای است که عنوان ستون یا سطر است.

## تصویر و ویدئو

```html
<!DOCTYPE html>

<!-- Demonstrates image -->

<html lang="en">
    <head>
        <title>image</title>
    </head>
    <body>
        <img alt="photo of bridge" src="bridge.png">
    </body>
</html>
```

- `src="bridge.png"` مسیری است که فایل تصویر در آن پیدا می‌شود. ویژگی `alt` متنی جایگزین برای کسانی است که تصویر را نمی‌بینند.

```html
<!DOCTYPE html>

<!-- Demonstrates video -->

<html lang="en">
    <head>
        <title>video</title>
    </head>
    <body>
        <video controls muted>
            <source src="video.mp4" type="video/mp4">
        </video>
    </body>
</html>
```

- ویژگی `type` می‌گوید ویدئو از نوع `mp4` است. `controls` و `muted` هم به `video` داده شده‌اند.

> [!TIP]
> **تألیفی: ویژگی بولی**
> `controls`، `muted` و `autofocus` (یادداشت بعد) مقدار ندارند: وجودشان یعنی «روشن» و نبودشان یعنی «خاموش». به این‌ها **ویژگی بولی** (`boolean attribute`) می‌گویند. نوشتن `muted="false"` آن را خاموش نمی‌کند؛ هنوز وجود دارد.

## پیوند

```html
<!DOCTYPE html>

<!-- Demonstrates link -->

<html lang="en">
    <head>
        <title>link</title>
    </head>
    <body>
      Visit <a href="image.html">Harvard</a>.
    </body>
</html>
```

- برچسب `<a>` یا **لنگر** (`anchor`) متن `Harvard` را قابل کلیک می‌کند و `href` مقصد را مشخص می‌کند.

> [!WARNING]
> **از سخنرانی: پیوندی که دروغ می‌گوید**
> دیوید نشان می‌دهد `href` جایی است که می‌روی و متن میان برچسب‌ها چیزی است که کاربر می‌بیند؛ این دو لازم نیست یکی باشند. می‌شود متن را نشانی هاروارد نوشت ولی `href` را به yale.edu داد. فیشینگ (phishing) از همین استفاده می‌کند؛ پیش از کلیک، نشانی واقعی را با بردن نشانگر روی پیوند ببین.

## اشتباه‌های رایج

- انتظار سطر جدید از Enter در کد HTML.
- جا انداختن `alt` در تصویرها.
- انتخاب سطح عنوان بر اساس اندازهٔ دلخواه.
- اعتماد به متن پیوند به جای `href`.

## جمع‌بندی

- `p` پاراگراف، `h1` تا `h6` عنوان‌ها، `ul`/`ol` با `li` فهرست‌ها.
- `table` با `tr` (سطر) و `td` (خانه) جدول می‌سازد.
- `img` با `src` و `alt`، `video` با `source` و ویژگی‌های بولی.
- `a` با `href` پیوند می‌سازد.

## پیوندها

- قبلی: [HTML: تگ، ویژگی و درخت سند](/kb/d/w08-n07)
- بعدی: [فرم‌ها: form و input](/kb/d/w08-n09)
- واژه‌نامه: `curriculum/glossary.fa.json` · منابع: `weeks/week-08/sources.json`

---

*Based on CS50x 2026 © David J. Malan, Harvard University (https://cs50.harvard.edu/x/), licensed CC BY-NC-SA 4.0. Persian rewrite and authored material by CS50x Anzali; same license (ShareAlike), non-commercial.*
