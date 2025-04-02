/**
 * blog.js - اسکریپت مدیریت قابلیت‌های وبلاگ
 * توابع جستجو و مرتب‌سازی مقالات
 */

// تابع برای ایجاد کوئری‌استرینگ با پارامترهای موجود و جدید
function createQueryString(params) {
    // دریافت پارامترهای فعلی URL
    const urlParams = new URLSearchParams(window.location.search);
    
    // به‌روزرسانی یا اضافه کردن پارامترهای جدید
    for (const key in params) {
        if (params[key] !== null && params[key] !== '') {
            urlParams.set(key, params[key]);
        } else {
            urlParams.delete(key);
        }
    }
    
    // حذف پارامتر صفحه اگر جستجو یا مرتب‌سازی جدید انجام شده
    if (params.hasOwnProperty('q') || params.hasOwnProperty('sort')) {
        urlParams.delete('page');
    }
    
    return urlParams.toString();
}

// تابع برای مدیریت جستجو
function handleSearch() {
    const searchInput = document.querySelector('.custom-search-input');
    const searchValue = searchInput.value.trim();
    
    // ایجاد کوئری‌استرینگ و هدایت کاربر
    const queryString = createQueryString({ q: searchValue });
    window.location.href = `${window.location.pathname}?${queryString}`;
}

// تابع برای مدیریت مرتب‌سازی
function handleSort(value) {
    // نگاشت مقادیر select به پارامتر sort
    const sortMap = {
        '1': 'newest',   // جدیدترین
        '2': 'oldest',   // قدیمی‌ترین
        '3': 'popular'   // پربازدیدترین
    };
    
    const sortValue = sortMap[value] || '';
    
    // ایجاد کوئری‌استرینگ و هدایت کاربر
    const queryString = createQueryString({ sort: sortValue });
    window.location.href = `${window.location.pathname}?${queryString}`;
}

// تابع برای مدیریت صفحه‌بندی
function changePage(pageNumber) {
    const queryString = createQueryString({ page: pageNumber });
    window.location.href = `${window.location.pathname}?${queryString}`;
}

// اجرای کد پس از بارگذاری صفحه
document.addEventListener('DOMContentLoaded', function() {
    // دریافت المان‌های مورد نیاز
    const searchButton = document.getElementById('button-search');
    const searchInput = document.querySelector('.custom-search-input');
    const sortSelect = document.getElementById('inputGroupSort');
    
    // پر کردن مقدار فیلد جستجو از پارامتر URL
    const urlParams = new URLSearchParams(window.location.search);
    const searchQuery = urlParams.get('q');
    if (searchQuery) {
        searchInput.value = searchQuery;
    }
    
    // پر کردن مقدار select مرتب‌سازی از پارامتر URL
    const sortValue = urlParams.get('sort');
    if (sortValue) {
        const sortValueMap = {
            'newest': '1',
            'oldest': '2',
            'popular': '3'
        };
        if (sortValueMap[sortValue]) {
            sortSelect.value = sortValueMap[sortValue];
        }
    } else {
        // اگر پارامتر sort در URL نباشد، به طور پیش‌فرض "جدیدترین" را انتخاب کن
        // توجه: وقتی هیچ sort انتخاب نشده، سرور به صورت پیش‌فرض مرتب‌سازی جدیدترین را اعمال می‌کند
        sortSelect.value = '1';
    }
    
    // رویداد کلیک دکمه جستجو
    if (searchButton) {
        searchButton.addEventListener('click', handleSearch);
    }
    
    // رویداد فشردن Enter برای جستجو
    if (searchInput) {
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                handleSearch();
            }
        });
    }
    
    // رویداد تغییر در select مرتب‌سازی
    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            handleSort(this.value);
        });
    }
}); 