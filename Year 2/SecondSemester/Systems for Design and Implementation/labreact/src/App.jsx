import React, {useEffect} from 'react';
import {useState} from 'react';
import ProbaTable from './ProbaTable.jsx';
import './App.css'
import ProbaForm from "./ProbaForm.jsx";
import {GetProbe, DeleteProba, AddProba, UpdateProba} from './utils/rest-calls'

export default function App() {
    const [probe, setProbe] = useState([{

        "nume": "ALERGARE",
        "arbitru": {
            "id": 2,
            "nume": "marian",
            "username": "mari",
            "parola": "caine"
        }
    }

    ]);

    function addFunc(proba){
        console.log('inside add Func' + proba);
        AddProba(proba)
            .then(res=>GetProbe())
            // n ar trebui sa fie setProbe(res)????
            .then(probe=>setProbe(probe))
            .catch(error=>console.log('eroare add ',error));
    }

    function deleteFunc(proba){
        console.log('inside deleteFunc ' +proba);
        DeleteProba(proba)
            .then(res=>GetProbe())
            .then(probe=>setProbe(probe))
            .catch(error=>console.log('eroare delete', error));
    }

    function updateFunc(proba){
        console.log('inside updateFunc' +proba);
        UpdateProba(proba)
            .then(res=>GetProbe())
            .then(probe=>setProbe(probe))
            .catch(error=>console.log('eroare update', error));
    }

    useEffect(()=>{
        console.log('inside useEffect')
        GetProbe().then(probe=>setProbe(probe));},[]);

    return (<div className="UserApp">
        <h1> Aplicatie Probe Triatlon </h1>
        <ProbaForm addFunc={addFunc} updateFunc={updateFunc}/>
        <br/>
        <br/>
        <ProbaTable probe={probe} deleteFunc={deleteFunc} />
    </div> );
}


