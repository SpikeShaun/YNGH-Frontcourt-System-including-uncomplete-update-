/**
 * 营业时间：每日 09:00 - 17:00
 */

function checkBusinessTime() {
    const now = new Date();
    const hour = now.getHours();
    const minute = now.getMinutes();

    const isOpen = (hour > 9 || (hour === 9 && minute >= 0)) &&
                   (hour < 17 || (hour === 17 && minute === 0));

    return isOpen;
}

function disablePageForOutOfTime() {
    // 添加顶部提示
    const alertDiv = document.createElement("div");
    alertDiv.className = "alert alert-danger text-center m-0";
    alertDiv.innerText = "⚠️ 当前为非投标时间（每日 09:00 - 17:00），请在营业时间内操作";
    document.body.prepend(alertDiv);

    // 禁用所有输入框、按钮等
    const elements = document.querySelectorAll("input, select, textarea, button");
    elements.forEach(el => {
        el.disabled = true;
        el.classList.add("disabled");
    });
}

function startTimeGuard(intervalMinutes = 2) {
    function runCheck() {
        if (!checkBusinessTime()) {
            disablePageForOutOfTime();
        }
    }

    // 初次加载立即检查
    runCheck();

    // 每 intervalMinutes 分钟检查一次
    setInterval(runCheck, intervalMinutes * 60 * 1000);
}

// 页面加载后执行
window.addEventListener("DOMContentLoaded", () => {
    const enableCheck = document.body.getAttribute("data-check-time") === "true";
    if (enableCheck) {
        startTimeGuard(1);  // 每1分钟检查一次
    }
});
