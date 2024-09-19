
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('main-content');
    const openBtn = document.querySelector('.open-btn');

    sidebar.classList.toggle('show');
    mainContent.classList.toggle('sidebar-hidden');

    // Mostrar ou esconder o botão de abrir dependendo do estado do menu
    if (window.innerWidth > 768) {
        // Mostrar ou esconder o botão de abrir no desktop
        openBtn.style.display = sidebar.classList.contains('show') ? 'none' : 'block';
    }
}

window.onload = function() {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('main-content');
    const openBtn = document.querySelector('.open-btn');

    if (window.innerWidth <= 768) {
        sidebar.classList.remove('show'); // Garante que o menu comece fechado no mobile
        mainContent.classList.add('sidebar-hidden');
        openBtn.style.display = 'block'; // Garante que o botão de abrir apareça no mobile
    } else {
        sidebar.classList.add('show'); // Garante que o menu esteja visível no desktop
        mainContent.classList.remove('sidebar-hidden');
        openBtn.style.display = 'none'; // Oculta o botão de abrir no desktop
    }
};

window.onresize = function() {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('main-content');
    const openBtn = document.querySelector('.open-btn');

    if (window.innerWidth > 768) {
        sidebar.classList.add('show'); // Garante que o menu esteja visível no desktop
        mainContent.classList.remove('sidebar-hidden');
        openBtn.style.display = 'none'; // Oculta o botão de abrir no desktop
    } else {
        sidebar.classList.remove('show'); // Garante que o menu comece fechado no mobile
        mainContent.classList.add('sidebar-hidden');
        openBtn.style.display = 'block'; // Garante que o botão de abrir apareça no mobile
    }
};
