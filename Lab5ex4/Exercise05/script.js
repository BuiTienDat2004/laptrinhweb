async function getWeather() {
  const city = document.getElementById("cityInput").value.trim();
  const apiKey = "YOUR_API_KEY"; // 🔁 Replace this with your real API key
  const weatherInfo = document.getElementById("weatherInfo");

  if (!city) {
    weatherInfo.innerText = "Please enter a city name.";
    return;
  }

  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

  try {
    const res = await fetch(url);
    const data = await res.json();

    if (data.cod === 200) {
      const temp = data.main.temp;
      const desc = data.weather[0].description;
      const icon = data.weather[0].icon;

      weatherInfo.innerHTML = `
        <p><strong>${data.name}</strong></p>
        <p>${desc} - ${temp}°C</p>
        <img src="https://openweathermap.org/img/wn/${icon}@2x.png" alt="weather icon">
      `;
    } else {
      weatherInfo.innerText = "City not found!";
    }
  } catch (error) {
    weatherInfo.innerText = "Error fetching data.";
    console.error(error);
  }
}
