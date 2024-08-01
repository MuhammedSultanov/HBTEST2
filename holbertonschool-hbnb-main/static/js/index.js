
document.addEventListener('DOMContentLoaded', () => {
    checkAuthentication();
    //populateCountryFilter();
});

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
        loginLink.style.display = 'block';
    } else {
        loginLink.style.display = 'none';
        fetchPlaces(token);
    }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}





async function fetchPlaces(token) {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            }
            
        });

        if (response.ok) {
            const data = await response.json();
            // displayPlaces(data);
            console.log('fetch worked')
            console.log(data)
        } else {
            console.error('Failed to fetch places');
        }
    } catch (error) {
        console.error('Error fetching places:', error);
    }
}

function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    placesList.innerHTML = '';

    places.forEach(place => {
        const placeElement = document.createElement('div');
        placeElement.className = 'place';
        placeElement.dataset.country = place.country;
        placeElement.innerHTML = `
            <h3>${place.name}</h3>
            <p>${place.description}</p>
            <p><strong>Location:</strong> ${place.location}</p>
        `;
        placesList.appendChild(placeElement);
    });
}



/*
function populateCountryFilter() {
    const countryFilter = document.getElementById('country-filter');
    // Assuming we have a predefined list of countries. This can also be fetched dynamically.
    const countries = ['USA', 'Canada', 'UK', 'Australia'];

    countries.forEach(country => {
        const option = document.createElement('option');
        option.value = country;
        option.textContent = country;
        countryFilter.appendChild(option);
    });

    countryFilter.addEventListener('change', (event) => {
        const selectedCountry = event.target.value;
        filterPlacesByCountry(selectedCountry);
    });
}

function filterPlacesByCountry(country) {
    const places = document.querySelectorAll('.place');
    places.forEach(place => {
        if (country === '' || place.dataset.country === country) {
            place.style.display = 'block';
        } else {
            place.style.display = 'none';
        }
    });
}



*/