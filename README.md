# SE-lab-HW9

Mohammad Cheraghi - 98105676

Reza Alipour - 98105932


## گزارش آزمایش

<p dir="rtl"  style='text-align: right;'>
  در این آزمایش ما سعی می‌کنیم با استفاده از معماری میکروسرویس یک سرویس را با استفاده از فریمورک Django و با استفاده از Docker بالا بیاوریم. در این پروژه دو میکروسرویس داریم که وظایف این دو میکروسرویس بدین شرح هستند: میکروسرویس اول وظیفه آن را دارد که قیمت دلاری هر توکن را با استفاده از یک سرویس خارجی بدست بیاورد. همچنین وظیفه میکرو سرویس دوم این است که که قیمت هر توکن را به نسبت توکن دیگر بدست بیاورد و محاسبه کند که به ازای مقداری از توکن اول، کاربر چقدر توکن از نوع دوم می‌تواند دریافت کند که این میکروسرویس این محاسبات را با استفاده از میکروسرویس اول انجام می‌دهد.
</p>

<p dir="rtl"  style='text-align: right;'>
  در دو تصویر زیر محتویات Dockerfile مربوط به میکروسرویس اول و دوم را مشاهده می‌کنیم که با توجه به موارد گفته شده در ویدیو ساخته شده‌اند. 
</p>

<img width="538" alt="Screenshot 1402-03-15 at 23 04 38" src="https://github.com/Reza-Alipour/SE_Lab9/assets/56475612/8842cef7-f773-40a3-a607-3910b173a93e">
<img width="533" alt="Screenshot 1402-03-15 at 23 04 46" src="https://github.com/Reza-Alipour/SE_Lab9/assets/56475612/3d66c3c5-9f65-4e7d-a22b-bce004b91f4c">

<p dir="rtl"  style='text-align: right;'>
در تصویر زیر محتویات فایل docker-compose را مشاهده می‌کنیم. از این ابزار برای راحتی کار با سرویس‌ها و اجرای آن‌ها همچنین ساختن یک شبکه بین سرویس‌ها استفاده می‌کنیم. در این فایل مشخصات دو سرویس مورد نظرمان، پورت‌هایی از container که باید به پورت سیستم عامل اصلی forward شوند و شبکه بین container ها مشخص شده است.
</p>
<img width="532" alt="Screenshot 1402-03-15 at 23 04 57" src="https://github.com/Reza-Alipour/SE_Lab9/assets/56475612/c370d994-5e95-4d5e-b498-3ed05671a2cc">

<p dir="rtl"  style='text-align: right;'>
  در دو تصویر زیر با استفاده از دستوراتی که در ویدیو نیز مشاهده شده اقدام به build کردن Dockerfileها می‌کنیم.
</p>
<img width="1139" alt="Screenshot 1402-03-15 at 23 05 20" src="https://github.com/Reza-Alipour/SE_Lab9/assets/56475612/476b339b-955d-47e2-8425-69437f860e3c">
<img width="1139" alt="Screenshot 1402-03-15 at 23 05 33" src="https://github.com/Reza-Alipour/SE_Lab9/assets/56475612/93c1d638-5ef1-4436-aaea-50ae0b4764e2">

<p dir="rtl"  style='text-align: right;'>
  همچنین برای راحتی می‌توانستیم مستقیم از دستور docker-compose build برای build کردن هر دو Dockerfile استفاده کنیم. 
</p>
<img width="1139" alt="Screenshot 1402-03-15 at 23 05 59" src="https://github.com/Reza-Alipour/SE_Lab9/assets/56475612/23a008ad-23d9-4dac-8912-128b04593bd1">

<p dir="rtl"  style='text-align: right;'>
  در این مرحله سعی می‌کنیم image های ساخته شده را اجرا کنیم. می‌توان دو image ساخته شده را به صورت مجزا اجرا کرد اما برای راحتی و برای اینکه شبکه داخلی دو container درست تنظیم شوند با استفاده از دستور docker-compose up سعی می‌کنیم هر دو میکروسرویس را همزمان اجرا کنیم. نتیجه‌ی اجرای این دستور و اجرای این دو میکروسرویس در تصویر زیر قابل مشاهده است. 
</p>
<img width="1139" alt="Screenshot 1402-03-15 at 23 06 19" src="https://github.com/Reza-Alipour/SE_Lab9/assets/56475612/8f1be2c8-b5f6-46bb-897d-e3b89c6f550e">

<p dir="rtl"  style='text-align: right;'>
  در دو تصویر زیر همانطور که خواسته شده خروجی دو دستور docker ps و docker image ls نمایش داده شده است. با استفاده از دستور docker ps می‌توان دو container مربوط به میکروسرویس‌ها را می‌توان مشاهده کرد که در حال اجرا هستند همچنین با استفاده از دستور docker image ls تمامی image هایی که برای این دو میکروسرویس ساخته شده و یا pull شده‌اند نیز قابل مشاهده هستند. 
</p>
<img width="1139" alt="Screenshot 1402-03-15 at 23 09 10" src="https://github.com/Reza-Alipour/SE_Lab9/assets/56475612/9e389c82-614a-47ad-8b98-d31e33bf1eb2">

<p dir="rtl"  style='text-align: right;'>
در سه تصویر زیر سعی شده با استفاده از برنامه postman و rest call زدن به میکروسرویس اول قیمت ۳ توکن مختلف گرفته شود. همانطور که مشاهده می‌شود میکروسرویس موردنظر به درستی قیمت سه توکن مختلف BTC, ETH, BSC را برگردانده. 
</p>
<img width="770" alt="Screenshot 1402-03-15 at 23 13 42" src="https://github.com/Reza-Alipour/SE_Lab9/assets/56475612/469f95e3-a6aa-4061-8f20-a637fe44041c">
<img width="770" alt="Screenshot 1402-03-15 at 23 07 57" src="https://github.com/Reza-Alipour/SE_Lab9/assets/56475612/b017f99d-8865-47ae-8a7d-e5d2d486ec7c">
<img width="770" alt="Screenshot 1402-03-15 at 23 13 56" src="https://github.com/Reza-Alipour/SE_Lab9/assets/56475612/332576f5-f566-4df7-974a-48fb9362ae41">
<p dir="rtl"  style='text-align: right;'>
  در دو تصویر زیر نیز با استفاده از postman سعی کردیم میکروسرویس دوم را تست کنیم. در پاسخ این درخواست‌ها قیمت دو توکن به دلار برگردانده شده و همچنین مشخص شده به ازای مقداری از توکن اول کاربر می‌تواند چه مقدار توکن دوم را دریافت کند.
</p>
<img width="770" alt="Screenshot 1402-03-15 at 23 07 24" src="https://github.com/Reza-Alipour/SE_Lab9/assets/56475612/f265e3d2-0c56-4bb7-be6a-617086343294">
<img width="770" alt="Screenshot 1402-03-15 at 23 07 05" src="https://github.com/Reza-Alipour/SE_Lab9/assets/56475612/183b9cc1-2a04-4c6e-8d25-3dd9d2bdb269">

