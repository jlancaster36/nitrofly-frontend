import { getStorage, ref, getDownloadURL } from "firebase/storage";

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBDbgHUYImNeapL2bFBW2CEwNaeIBaaZIk",
  authDomain: "nitrofly-2f5d0.firebaseapp.com",
  projectId: "nitrofly-2f5d0",
  storageBucket: "nitrofly-2f5d0.appspot.com",
  messagingSenderId: "958552361171",
  appId: "1:958552361171:web:e633bc03086c8fd7a4ac26",
  measurementId: "G-Z3NQH7KNGR"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
// var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

/**
 * Construct the file path string used in the reference calls
 * @param {String} system Usually 3 char string denoting console (e.g. GBA, N64)
 * @param {String} name Name of the game whose data is being retreived (as named in firebase)
 * @param {boolean} rom Boolean value of whether we want to download the rom from firebase if present at all
 * @returns An array of strings for ref() in format [box2d, video, support, rom (if true)]
 */
function constuctRefs(system, name, rom = false){
    const box2d = "Metadata/" + system + "/box2dfront/" + name + ".png";
    const video = "Metadata/" + system + "/video/" + name + ".mp4";
    const support = "Metadata/" + system + "/support/" + name + ".png";

    if(rom == true) {
        const rom = "Roms/" + system + "/" + name + ".gba";
        return [box2d, video, support, rom];
    }
    return [box2d, video, support, false];
}

/**
 * 
 * @param {*} name 
 * @param {*} system 
 * @param {*} rom 
 */
function downloadMetadata(name, system, rom = false) {
    const storage = getStorage();
    const storageRef = ref(storage);
    const paths = constuctRefs(system, name, true);
    const coverRef = ref(storage, paths[0]);
    const videoRef = ref(storage, paths[1]);
    const supportRef = ref(storage, paths[2]);
    // const romRef = ref(storage, paths[3]);

    /////////////

    downloadWrapper(coverRef, name + ".png");
    downloadWrapper(videoRef, name + ".mp4");
    downloadWrapper(supportRef, name + ".png");
    // downloadWrapper(romRef, name + ".gba");

}

import {DownloaderHelper} from 'node-downloader-helper';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
console.log(__filename);
const __dirname = dirname(__filename).slice(-8, -1) + "metadata";

console.log(__dirname);
function downloadWrapper(ref, name){
    getDownloadURL(ref)
    .then((url) => {
        // `url` is the download URL for 'images/stars.jpg'
        // const { DownloaderHelper } = require('node-downloader-helper');
        console.log(url);
        const dl = new DownloaderHelper(url, __dirname, {fileName: name});
        dl.on("end", () => console.log("Download complete"));
        dl.start();
    })
    .catch((error) => {
        console.log("error: " + error);
    });

}

function testDownload(){
    const name = "Metroid - Zero Mission (U) [!]";
    const system = "GBA";

    // Should download metadata to the metaData Dir in the app
    downloadMetadata(name, system);
}

testDownload();