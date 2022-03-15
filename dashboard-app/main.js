const {app, BrowserWindow} = require('electron')

const createWindow = () =>{
    const win = new BrowserWindow ({
        width: 800,
        height: 550
    })

    win.loadFile('index.html')
    win.setMenu(null)
}

app.whenReady().then(() => {
    createWindow()
})