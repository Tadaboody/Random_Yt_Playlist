chrome.browserAction.onClicked.addListener(function (tab) {
    console.log('icon clicked');
    open_url(yt_endpoint(),{new_window : true});
});
function yt_endpoint(...args) {
    base_url = "https://www.youtube.com"
    return args.reduce((acc, current) => acc + '/' + current, base_url);
}
function open_url(url, parameters={active : true, pinned : false, new_window : false}) {
    
    if (parameters.new_window) {
        chrome.windows.create({ url: url })
    }
    else {
        chrome.tabs.create({
            url: url,
            active: parameters.active,
            pinned: parameters.pinned
        });
    }
}