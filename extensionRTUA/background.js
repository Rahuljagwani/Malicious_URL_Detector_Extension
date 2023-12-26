chrome.action.onClicked.addListener((tab) => {
    chrome.scripting.executeScript({
      target: {tabId: tab.id},
      files: ['content.js']
    });
});

async function getCurrentTab() {
    let queryOptions = { active: true, lastFocusedWindow: true };
    let [tab] = await chrome.tabs.query(queryOptions);
    return tab;
  }

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    getCurrentTab()
    .then((response) => {
        sendResponse(response);
        chrome.tabs.remove(response.id);
        console.log(response.id);
    })
    .catch((err) => console.log(err));
    return true;
});