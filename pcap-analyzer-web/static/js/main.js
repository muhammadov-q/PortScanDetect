// Theme Switcher
const toggleSwitch = document.getElementById('theme-toggle');
const darkModeStylesheet = document.getElementById('dark-mode-css');

// Check localStorage for theme preference
if (localStorage.getItem('darkMode') === 'enabled') {
    darkModeStylesheet.disabled = false;
    toggleSwitch.checked = true;
}

toggleSwitch.addEventListener('change', function() {
    if (this.checked) {
        darkModeStylesheet.disabled = false;
        localStorage.setItem('darkMode', 'enabled');
    } else {
        darkModeStylesheet.disabled = true;
        localStorage.setItem('darkMode', 'disabled');
    }
});
