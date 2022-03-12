import React, { useState, useEffect } from 'react';
import Drop from 'components/dropdown/Drop';


       

const Tarifa = () => {
  const [nome, setNome] = useState('');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');
  const [nblocos, setBlocos] = useState('');
  const [zip, setZip] = useState('');
  //const [concessionaria, setConcessionaria] = useState('');
  //const [tarifa, setTarifa] = useState('');
  const [errors, setErrors] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (localStorage.getItem('token') !== null) {
      window.location.replace('http://localhost:3000/dashboard');
    } else {
      setLoading(false);
    }
  }, []);

  fetch('http://127.0.0.1:8000/tarifas/concessionarias/list/')
      .then(res => res.json())
      .then(data => {
        //console.log(data);
      });
  

  const onSubmit = e => {
    e.preventDefault();
    var empresa= document.getElementById('empresa');
    var tarifa = document.getElementById('tarifa');
    //var object = this.refs.empresa;
    const condo = {
      name: nome,
      phone: phone,
      email: email,
      num_blocos: nblocos,
      zip_code: zip,
      concessionaria: empresa.value,
      faixa: tarifa.value
    };
    //alert(aux.value)
    alert(JSON.stringify(condo));
    fetch('http://127.0.0.1:8000/api/v1/token/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(condo)
    });
};
    
    
  
  return (
    <div>
      {loading === false && <h1>Tarifas</h1>}
      {errors === true && <h2>Cannot log in with provided credentials</h2>}
      {loading === false && (
        <form onSubmit={onSubmit}>
          <label >Nome do condomínio:</label> <br />
          <input
            name='cond'
            //type='email'
            value={nome}
            //required
            onChange={e => setNome(e.target.value)}
          />{' '}
          <br />
          <label >Telefone para contato:</label> <br />
          <input
            name='phone'
            type='number'
            value={phone}
            //required
            onChange={e => setPhone(e.target.value)}
          />{' '}
          <br />
          <label >Email institucional:</label> <br />
          <input
            name='email'
            type='email'
            value={email}
            //required
            onChange={e => setEmail(e.target.value)}
          />{' '}
          <br />
          <label >Nº de blocos do condomínio:</label> <br />
          <input
            name='nblocos'
            type='number'
            value={nblocos}
            //required
            onChange={e => setBlocos(e.target.value)}
          />{' '}
          <br />
          <label >CEP:</label> <br />
          <input
            name='zip'
            type='number'
            value={zip}
            //required
            onChange={e => setZip(e.target.value)}
          />{' '}
          <br />
          <Drop />
          <input type='submit' value='Submeter' />
        </form>
      )}
    </div>
  );
};

export default Tarifa;
