document.getElementById('priceForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    const area = document.getElementById('area').value;
    const year = document.getElementById('year').value;

    const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ GrLivArea: area, YearBuilt: year }),
    });

    const result = await response.json();
    document.getElementById('result').textContent = `Predicted Price: $${result.price.toFixed(2)}`;
});
