const fetchGetUrl = 'http://127.0.0.1:8000/fruits/'

async function fetchTestGet() {
    const response = await fetch(fetchGetUrl)
    const fruits = await response.json()

    const list = document.getElementById('fruit-list')

    fruits.forEach((fruit) => {
        const li = document.createElement('li')
        li.textContent = `${fruit.name} - ${fruit.color} - ${fruit.weight} - ${fruit.price}`
        list.appendChild(li)
    })
}