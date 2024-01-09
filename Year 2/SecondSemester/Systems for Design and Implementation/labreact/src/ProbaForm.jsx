
import React from  'react';
import { useState } from 'react';

export default function ProbaForm({addFunc, updateFunc}){
    const [id, setId] = useState('');
    const [nume, setNume] = useState('');

    const [arbitruId, setArbitruId] = useState('');
    const [arbitru, setArbitru] = useState('');
    const [arbitruNume, setArbitruNume] = useState('');
    const [arbitruUsername, setArbitruUsername] = useState('');
    const [arbitruParola, setArbitruParola] = useState('');

    function handleSubmit(event){
        let proba={id:id,
        nume:nume,
        arbitru:{id:arbitruId, nume:arbitruNume,username:arbitruUsername, parola:arbitruParola}}

        console.log('a proba was submitted');
        console.log(proba);
        addFunc(proba);
        event.preventDefault();
    }


    function handleUpdate(event){
        let proba={id:id,
        nume:nume,
        arbitru:{id:arbitruId, nume:arbitruNume,username:arbitruUsername, parola:arbitruParola}}

        console.log('a proba was updated');
        console.log(proba);
        updateFunc(proba);
        event.preventDefault();
    }



    return(
        <form onSubmit={handleSubmit}>
            <label>
                Id:
                <input type="text" value={id} onChange={e=>setId(e.target.value)}/>
            </label><br/>
            <label>
                Nume:
                <input type="text" value={nume} onChange={e=>setNume(e.target.value)} />
            </label><br/>
            <label>
                Arbitru Id:
                <input type="text" value={arbitruId} onChange={e=>setArbitruId(e.target.value)} />
            </label><br/>
            <label>
                Arbitru Nume:
                <input type="text" value={arbitruNume} onChange={e=>setArbitruNume(e.target.value)} />
            </label><br/>
            <label>
                Arbitru Username:
                <input type="text" value={arbitruUsername} onChange={e=>setArbitruUsername(e.target.value)} />
            </label><br/>
            <label>
                Arbitru Parola:
                <input type="text" value={arbitruParola} onChange={e=>setArbitruParola(e.target.value)} />
            </label><br/>

            <input type="submit" value="Add proba"/>
            <input type="button" onClick={handleUpdate} value="update proba"/>
        </form>);
}