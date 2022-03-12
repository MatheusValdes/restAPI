import React from 'react';



class Drop extends React.Component {

    constructor(){
        super();
        this.state = {
            options: [],
            tarifa: [],
        }  
    }

    componentDidMount() {
        let empresas = [];
        fetch('http://127.0.0.1:8000/tarifas/concessionarias/list/')
            .then(response => {
                return response.json();
            }).then(data => {
            //empresas = data.results.map(() => {
            //    return data.results
            //});
            for(var i=0; i< data.length; i++){
                empresas.push(data[i].nome);
                //console.log(data[i])
            }
            
            
            //console.log(empresas);
            this.setState({
                options: empresas,
            });
        });
    }

    empresaChange = (event) => {
        //console.log("-----");
        
        let tarifas =[];
        this.setState({
            tarifa: tarifas,
        })
        var url = 'http://127.0.0.1:8000/tarifas/tarifas/list/'+event.target.value;
        //console.log(url);
        fetch(url)
            .then(response => {
                return response.json();
            }).then(data => {
                for(var i=0; i< data.length; i++){
                    tarifas.push(data[i].tarifa);
                    //console.log(data[i])
                }
                //console.log(tarifas);
                this.setState({
                    tarifa: tarifas,
                })
                
            });
    };

    render(){
        return <div className="drop-down" >
            <label>Selecione uma concessionária</label>
            <br/>
            <select onChange={this.empresaChange} id="empresa">
                <option>Concessionária</option>
                { this.state.options.map((option) => <option value={option} >{option}</option>) }
            </select>
            <br />
            <label>Selecione o tipo de tarifa</label>
            <br/>
            <select id="tarifa">
                <option>Tipo de tarifa</option>
                { this.state.tarifa.map((option) => <option value={option} >{option}</option>) }
            </select>
            </div>;
    }
}

export default Drop;