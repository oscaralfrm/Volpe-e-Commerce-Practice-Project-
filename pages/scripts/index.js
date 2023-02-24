const hamburgerMenu = document.getElementById('bar');
const navBar = document.getElementById('navbar');
const closeButton = document.getElementById('close');

if (hamburgerMenu) {
    hamburgerMenu.addEventListener('click', () => {
        navBar.classList.add('active');
        hamburgerMenu.classList.add('inactive');
    })
}

if (closeButton) {
    closeButton.addEventListener('click', () => {
        navBar.classList.remove('active');
        hamburgerMenu.classList.remove('inactive');
    })
}