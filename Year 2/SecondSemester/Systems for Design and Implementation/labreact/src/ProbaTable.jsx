import React from "react";
import './App.css'

function ProbaRow({proba, deleteFunc}){
    function handleDelete(event){
        console.log('delete button pentru '+proba.id);
        deleteFunc(proba.id);
    }


    return(
        <tr>
            <td>{proba.id}</td>
            <td>{proba.nume}</td>
            <td>{proba.arbitru.nume}</td>
            <td><button onClick={handleDelete}>Delete</button> </td>
        </tr>
    );
}

export default function ProbaTable({probe, deleteFunc}){
    console.log("In ProbeTable");
    console.log(probe);
    // let rows=[];
    // probe.forEach(function(proba){
    //     rows.push(<ProbaRow proba={proba} key={proba.id} deleteFunc={deleteFunc} /> );
    // });

    const rows = probe.map(proba=><ProbaRow proba={proba} deleteFunc={deleteFunc}/> )

    return(
        <div className="ProbaTable">
            <table className="center">
                <thead>
                <tr>
                    <th>Id</th>
                    <th>Nume</th>
                    <th>Arbitru</th>

                    <th> Actions </th>
                </tr>
                </thead>
                <tbody>{rows}</tbody>

            </table>
        </div>
    );
}