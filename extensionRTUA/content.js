const apiUrl = 'https://rahuljagwani.pythonanywhere.com/analyze';
const tabURL = location.href;
console.log(tabURL);
fetch(apiUrl, {
    method: 'POST',
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({"url": tabURL}),
})
.then(response => response.json())
.then(async (data) => {
    console.log(data);
    const valid = data.output;
    if (valid) {
        const confirmation = confirm("This webpage seems suspicious. Do you still want to continue?");
        if(!confirmation) {
            const response = await chrome.runtime.sendMessage({action: "primary"});
            console.log(response);
        }
    }
})
.catch((err) => { console.log(err) });