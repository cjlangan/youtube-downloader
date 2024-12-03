text = document.getElementById("title");
textbox = document.getElementById("textbox");
button = document.getElementById("button");

function buttonClick()
{
    url = textbox.value;
    textbox.value = "";

    fetch('/API/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
    })
    .then(response => {
        if(!response.ok) {
            throw new Error('Failed to download video');
        }
        return response.blob();
    })
    .then(blob => {
        const downloadUrl = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = downloadUrl;
        link.download = 'video.mp4';
        link.click();
        URL.revokeObjectURL(downloadUrl);
    })
    .catch(error => {
        console.error(error);
    });
}
