/*!
 * Color mode toggler for Bootstrap's docs (https://getbootstrap.com/)
 * Copyright 2011-2022 The Bootstrap Authors
 * Licensed under the Creative Commons Attribution 3.0 Unported License.
 */

(() => {
    'use strict';
    const getPreferredTheme = () => {
        const storedTheme = localStorage.getItem('theme');
        if (storedTheme) {
            return storedTheme;
        }

        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    };

    const setTheme = function (theme) {
        if (theme === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.documentElement.setAttribute('data-bs-theme', 'dark');
        } else {
            document.documentElement.setAttribute('data-bs-theme', theme);
        }
        localStorage.setItem('theme', theme);
    };

    function showActiveTheme() {
        document.querySelector('.theme-switcher').querySelectorAll('i').forEach(el => {
            el.classList.add('d-none');
        });
        const theme = getPreferredTheme();
        if (theme == 'auto') {
            document.querySelector('.theme-auto').classList.remove('d-none');
        } else if (theme == 'light') {
            document.querySelector('.theme-light').classList.remove('d-none');
        } else if (theme == 'dark') {
            document.querySelector('.theme-dark').classList.remove('d-none');
        }
        document.getElementById('color-theme-name').innerText = theme;
    }

    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
        const storedTheme = localStorage.getItem('theme');
        if (storedTheme !== 'light' || storedTheme !== 'dark') {
            setTheme(getPreferredTheme());
        }
    });

    window.addEventListener('DOMContentLoaded', () => {
        showActiveTheme(getPreferredTheme());

        let theme = localStorage.getItem('theme');
        let toggler = document.querySelector('.theme-switcher');

        toggler.onclick = function(e) {
            e.preventDefault();
            const themes = 'auto light dark'.split(' ');
            const theme = getPreferredTheme();
            const index = themes.indexOf(theme);
            const next = themes[index + 1] || themes[0];
            setTheme(next);
            showActiveTheme();
        };
    });

    setTheme(getPreferredTheme());
})();
