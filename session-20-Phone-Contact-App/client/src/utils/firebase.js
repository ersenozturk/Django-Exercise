// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDPmPqbZakJBkCYplgSHOYMUnyQU1SJwc0",
  authDomain: "fire-contact-app-572e4.firebaseapp.com",
  databaseURL: "https://fire-contact-app-572e4-default-rtdb.firebaseio.com",
  projectId: "fire-contact-app-572e4",
  storageBucket: "fire-contact-app-572e4.appspot.com",
  messagingSenderId: "550814411916",
  appId: "1:550814411916:web:6de3bfbe2be29d9de39fa9",
};

// Initialize Firebase
const firebase = initializeApp(firebaseConfig);

export default firebase;
