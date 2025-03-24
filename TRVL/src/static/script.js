function changeImage(destination) {
    const imageDiv = document.getElementById('destination-image');
    const title = document.getElementById('destination-title');

    if (destination === 'rio') {
        imageDiv.style.backgroundImage = "url('static/imgs/rio.jpg')";
        title.textContent = 'Rio de Janeiro';
    } else if (destination === 'sao') {
        imageDiv.style.backgroundImage = "url('static/imgs/sao-paulo.jpeg')";
        title.textContent = 'São Paulo';
    } else if (destination === 'gramado') {
        imageDiv.style.backgroundImage = "url('static/imgs/gramado.jpg')";
        title.textContent = 'Gramado';
    } else if (destination === 'belo') {
        imageDiv.style.backgroundImage = "url('static/imgs/belo-horizonte.jpg')";
        title.textContent = 'Belo Horizonte';
    } else if (destination === 'curitiba') {
        imageDiv.style.backgroundImage = "url('static/imgs/curitiba.jpg')";
        title.textContent = 'Curitiba';
    }

    // Remove the 'active' class from all buttons
    document.querySelectorAll('.destination-selection button').forEach(button => button.classList.remove('active'));

    // Add the 'active' class to the clicked button
    event.target.classList.add('active');
}
