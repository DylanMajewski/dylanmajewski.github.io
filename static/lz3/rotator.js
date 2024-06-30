document.addEventListener('DOMContentLoaded', function() {
    const image = document.getElementById('rotatableImage');
    let lastAngle = 0;
    let isFollowingMouse = true; // Default state is true to follow the mouse
    let rotationIntervalId = null; // To store the interval ID

    document.getElementById('toggleFollowMouse').addEventListener('click', function() {
        isFollowingMouse = !isFollowingMouse;
    });

    // Function to start rotation
    function startRotation(direction) {
        if (rotationIntervalId !== null) return; // Prevent multiple intervals
        rotationIntervalId = setInterval(() => {
            lastAngle += (direction === 'clockwise' ? 1 : -1); // Adjust rotation speed here
            image.style.transform = `rotate(${lastAngle}deg)`;
            document.getElementById('rotationAngleDisplay').textContent = `Rotation Angle: ${lastAngle.toFixed(2)}°`;
        }, 20); // Adjust rotation speed by changing the interval time
    }

    // Function to stop rotation
    function stopRotation() {
        clearInterval(rotationIntervalId);
        rotationIntervalId = null;
    }

    // Attach event listeners to buttons
    document.getElementById('rotateClockwise').addEventListener('mousedown', () => startRotation('clockwise'));
    document.getElementById('rotateCounterClockwise').addEventListener('mousedown', () => startRotation('counter-clockwise'));

    // Stop rotation when mouse is up
    document.getElementById('rotateClockwise').addEventListener('mouseup', stopRotation);
    document.getElementById('rotateCounterClockwise').addEventListener('mouseup', stopRotation);

    // Also consider stopping rotation when the mouse leaves the button area
    document.getElementById('rotateClockwise').addEventListener('mouseleave', stopRotation);
    document.getElementById('rotateCounterClockwise').addEventListener('mouseleave', stopRotation);

    document.addEventListener('keydown', function(event) {
        if (event.code === 'Space' || event.code === 'ArrowRight' || event.code === 'ArrowLeft') {
            event.preventDefault(); // Prevent the default action for these keys
            if (event.code === 'Space') {
                isFollowingMouse = !isFollowingMouse;
            } else if (event.code === 'ArrowRight') {
                startRotation('clockwise');
            } else if (event.code === 'ArrowLeft') {
                startRotation('counter-clockwise');
            }
        }
    });
    
        document.addEventListener('keyup', function(event) {
            if (event.code === 'ArrowRight' || event.code === 'ArrowLeft') {
                stopRotation();
            }
        });

    document.addEventListener('mousemove', function(e) {
        if (!isFollowingMouse) return; // Exit if not following mouse

        const rect = image.getBoundingClientRect();
        const imageCenterX = rect.left + rect.width / 2;
        const imageCenterY = rect.top + rect.height / 2;
        const angleDeg = angle(imageCenterX, imageCenterY, e.clientX, e.clientY);

        // Calculate the shortest rotation path
        let diff = angleDeg - lastAngle;
        diff += (diff > 180) ? -360 : (diff < -180) ? 360 : 0;
        lastAngle += diff;
        image.style.transform = `rotate(${lastAngle}deg)`;

        document.getElementById('rotationAngleDisplay').textContent = `Rotation Angle: ${lastAngle.toFixed(2)}°`;
    });

    function angle(cx, cy, ex, ey) {
        const dy = ey - cy;
        const dx = ex - cx;
        const rad = Math.atan2(dy, dx); // range (-PI, PI]
        const deg = rad * (180 / Math.PI); // rads to degs, range (-180, 180]
        return deg;
    }
});