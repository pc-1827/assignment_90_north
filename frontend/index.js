// Toggle Left Menu
toggleBtn.addEventListener('click', () => {
    leftMenu.classList.toggle('collapsed');
    // Toggle the text and icon
    if (leftMenu.classList.contains('collapsed')) {
        toggleBtn.textContent = '☰'; // Only icon
        leftMenuList.style.display = 'none'; // Hide menu list
    } else {
        toggleBtn.textContent = '☰ Toggle Menu'; // Icon with text
        leftMenuList.style.display = 'block'; // Show menu list
    }
});

function shrinkPage() {
    const width = window.innerWidth;
    let scale = 1;

    if (width >= 992 && width <= 1600) {
        scale = 0.9;
    } else if (width >= 700 && width <= 767) {
        scale = 0.8;
    } else if (width >= 600 && width < 700) {
        scale = 0.75;
    } else if (width <= 600) {
        scale = 0.5;
    } else {
        scale = 1;
    }

    wrapper.style.transform = `scale(${scale})`;
}
// Initial shrink on page load
window.addEventListener('load', shrinkPage);

// Shrink on window resize
window.addEventListener('resize', shrinkPage);
