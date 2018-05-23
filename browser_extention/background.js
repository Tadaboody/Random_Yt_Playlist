chrome.browserAction.onClicked.addListener(function (tab) {
    console.log('icon clicked');
    get_yt_html(
        (html) => {
            const playlist_list = get_playlists(html);
            const chosen_playlist = unescape(JSON.parse('"' + choose(playlist_list))); //Unescape unicode characters like \\u200;
            open_url(yt_endpoint(chosen_playlist));
        }
    );
    // open_url(yt_endpoint(),{new_window : true});
});

function choose(array)
{
    return array[Math.floor(Math.random() * array.length)];
}
function yt_endpoint(...args) {
    const base_url = "https://www.youtube.com";
    return args.reduce((acc, current) => acc + '/' + current, base_url);
}

function get_yt_html(cb) {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", yt_endpoint());
    xhr.onloadend = () => {
        if (xhr.status == 200) {
            cb(xhr.responseText);
        }

    };
    xhr.send();
    return xhr.responseText;
}

function get_playlists(html)
{
    const playlist_regex = /(watch\?v=[^\"]+list=[^\"]+)\"/g;
    const playlist_list = html.match(playlist_regex);
    console.log(playlist_list);
    return playlist_list;
}

function open_url(url, parameters={active : true, pinned : false, new_window : false}) {
    
    if (parameters.new_window) {
        chrome.windows.create({ url: url });
    }
    else {
        chrome.tabs.create({
            url: url,
            active: parameters.active,
            pinned: parameters.pinned
        });
    }
}