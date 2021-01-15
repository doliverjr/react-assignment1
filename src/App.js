import React, { Component } from 'react'
import axios from 'axios'
import Table from './Table'
import Form from './Form';

class App extends Component {

    componentDidMount() {
        axios.get('http://localhost:5000/users')
            .then(res => {
                const characters = res.data.users_list;
                this.setState({ characters });
            })
        .catch(function (error) {
            //Not handling the error. Just logging into the console.
            console.log(error);
        });
    }

    state = {
        characters: []
    }


//Remove entry from table
//Takes an index, and makes call to makeDeleteCall to delete an entry
//Updates table if item was deleted, does nothing if DELETE failed
    removeCharacter = index => {
        const {characters} = this.state
        this.makeDeleteCall(this.state.characters[index]).then( callResult => {
            if (callResult === true) {
                this.setState({
                    characters: characters.filter((character, i) => {
                        return i !== index
                    })
                })
            }
        });
    }

//Makes call using axios to delete an entry
//Logs error if delete does not return code 200
    makeDeleteCall(character){
        return axios.delete('http://localhost:5000/users', {data: character})
            .then(function (response) {
                console.log(response);
                return (response.status === 200);
            })
            .catch(function (error) {
                console.log(error);
                return false;
            });
    }

//Add new entry to table
//Takes an character, and makes call to makePostCall to add an entry
//Updates table if item added to table, does nothing if POST failed
    handleSubmit = character => {
        this.makePostCall(character).then( response => {
            if (response.status === 201) {
                console.log(response)
                this.setState({ characters: [...this.state.characters, response.data] });
            }
        });
    }

//makes call using axios to add an entry
//Logs error if POST does not return code 201
    makePostCall(character){
        return axios.post('http://localhost:5000/users', character)
            .then(function (response) {
                console.log(response);
                return (response);
            })
            .catch(function (error) {
                console.log(error);
                return error;
            });
    }

    render() {
        const { characters } = this.state

        return (
            <div className="container">
            <Table characterData={characters} removeCharacter={this.removeCharacter} />
            <Form handleSubmit={this.handleSubmit} />
            </div>
        )
    }
}


export default App