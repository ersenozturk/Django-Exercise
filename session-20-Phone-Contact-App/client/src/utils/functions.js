// Database bilgi ekleme,bilgiyi alma, bilgi silme ve değiştirme
import firebase from "./firebase";
import { useState, useEffect } from "react";
import {
  getDatabase,
  ref,
  set,
  push,
  onValue,
  remove,
  update,
} from "firebase/database";
import Toastify from "./toast";

let updateContacts;

// Bilgi Ekleme
export const AddUser = (info) => {
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  const raw = JSON.stringify({
    username: info.username,
    phoneNumber: info.phoneNumber,
    gender: info.gender,
  });

  const requestOptions = {
    method: "POST",
    headers: myHeaders,
    body: raw,
    redirect: "follow",
  };

  fetch("http://127.0.0.1:8000/api/contact/", requestOptions)
    .then((response) => response.text())
    .then((result) => {
      console.log(result);
      updateContacts();
    })
    .catch((error) => console.log("error", error));

  // const db = getDatabase();
  // const userRef = ref(db, "baglanti");
  // const newUserRef = push(userRef);
  // set(newUserRef, {
  //   username: info.username,
  //   phoneNumber: info.phoneNumber,
  //   gender: info.gender,
  // });
};

// Bilgi Çağırma

export const useFetch = () => {
  const [isLoading, setIsLoading] = useState();
  const [contactList, setContactList] = useState();

  const getContacts = () => {
    fetch("http://127.0.0.1:8000/api/contact/")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setContactList(data);
        setIsLoading(false);
      })
      .catch((err) => console.log(err));
  };

  updateContacts = getContacts;

  useEffect(() => {
    setIsLoading(true);

    getContacts();

    // const db = getDatabase();
    // const userRef=ref(db,"baglanti");

    // onValue(userRef, (snapshot) => {
    //     const data = snapshot.val();
    //     const baglantiArray=[];

    //     for(let id in data){
    //         baglantiArray.push({id,...data[id]})
    //     }
    //     setContactList(baglantiArray);
    //     setIsLoading(false);
    // });
  }, []);
  return { isLoading, contactList, getContacts };
};

// Bilgi silme
export const DeleteUser = (id) => {
  // const db = getDatabase();
  // const userRef = ref(db, "baglanti");
  // remove(ref(db, "baglanti/" + id));

  fetch("http://127.0.0.1:8000/api/contact/" + id + "/", { method: "DELETE" })
    .then((response) => response.text())
    .then((result) => {
      console.log(result);
      updateContacts();
    })
    .catch((error) => console.log("error", error));

  Toastify("Kullanıcı bilgisi silindi");
};

// Bilgi Değiştirme

export const EditUser = (info) => {
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  const raw = JSON.stringify({
    ...info,
  });

  const requestOptions = {
    method: "PUT",
    headers: myHeaders,
    body: raw,
    redirect: "follow",
  };

  fetch("http://127.0.0.1:8000/api/contact/" + info.id + "/", requestOptions)
    .then((response) => response.text())
    .then((result) => {
      console.log(result);
      updateContacts();
    })
    .catch((error) => console.log("error", error));
  // const db = getDatabase();
  // const updates = {};

  // updates["baglanti/" + info.id] = info;
  // return update(ref(db), updates);
};
