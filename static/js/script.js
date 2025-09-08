// 自动倒计时跳转（用于 success_page.html）
function startCountdown(seconds, redirectUrl) {
    const countdownEl = document.getElementById("countdown");
    if (!countdownEl) return;

    function tick() {
        if (seconds <= 0) {
            window.location.href = redirectUrl;
        } else {
            countdownEl.innerText = seconds;
            seconds--;
            setTimeout(tick, 1000);
        }
    }

    tick();
}

// 判断是否在营业时间（每日 09:00 ~ 17:00）
function isBusinessHour() {
    const now = new Date();
    const hour = now.getHours();
    const minute = now.getMinutes();
    return (hour > 9 || (hour === 9 && minute >= 0)) && (hour < 17 || (hour === 17 && minute === 0));
}

// 灰掉页面上的所有输入、按钮
function disableAllInputs() {
    const inputs = document.querySelectorAll('input, select, textarea, button');
    inputs.forEach(el => {
        el.disabled = true;
        el.classList.add('disabled');
    });

    const alertBox = document.createElement('div');
    alertBox.className = 'alert alert-danger mt-3';
    alertBox.innerText = '⚠️ 当前为非投标时间（每日 09:00~17:00），暂不开放填写';
    document.body.prepend(alertBox);
}

// 自动执行检查
window.addEventListener("DOMContentLoaded", () => {
    const enableBusinessCheck = document.body.getAttribute("data-check-time") === "true";

    if (enableBusinessCheck && !isBusinessHour()) {
        disableAllInputs();
    }
});
