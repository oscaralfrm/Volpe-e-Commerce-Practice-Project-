
/* Navbar Scripts */

const hamburgerMenu = document.getElementById('bar');
const navBar = document.getElementById('navbar');
const closeButton = document.getElementById('close');
const myAccount = document.getElementById('my-account');
const accountOptions = document.getElementById('account-options');


/* Function when handling responsive menus  // Navbar Hamburger Menu */
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

/* Toggle My Account Options - Desktop View */ 

if (myAccount) {
    myAccount.addEventListener('mouseover', () => {
        accountOptions.classList.add('active');
    })
}

if (accountOptions) {
    accountOptions.addEventListener('mouseleave', () => {
        accountOptions.classList.remove('active');
    })
}