import { useState } from 'react';
import {ParserResults,LexerResults,LexerResultsModal} from './components';
import {sintacticoService , lexerService} from './_services'
function App() {
  const [input,setInput] = useState("");
  const [action,setAction] = useState("");
  const [parseObject,setParseObject] = useState(null)
  const [l_list,setL_list] = useState([])
  const [line_list,setLine_list] = useState([])
  const [showModal,setShowModal] = useState(false)
  const [index_token,setIndex_token] = useState(0);

  function handleInput(event){
    setInput(event.target.value)
  }

  function viewModal(){
    setShowModal(!showModal)
  }

  

  function getColor(){
    sintacticoService.getAll(input).then(
      object=>{
        if(object=="Valid Syntax"){
          setParseObject({color:'green',text:object})
        }else{
          setParseObject( {color:'red',text:object})
        }
        setAction("parser")
      }, error=>{

      }
    )
  }

  function getTokens(){
    setLine_list(input.split('\n'))
    for(let line of input.split('\n')){
      lexerService.getAll(line).then(
        object=>{
          l_list.push(object)
        }  
      )
    }
    
    setL_list(l_list);
    setAction("lex")
    
  }

  function setIndexTok(idx){
    let data = l_list[idx]
    setIndex_token(data);
  }

  return (
    <div className="App p-24">
      <div className="flex flex-col">
        <header className="font-body text-4xl text-center">
          LEXER & PARSER VALIDATOR
        </header>
        <div className="grid grid-cols-2 h-full mt-5 px-40 gap-2">
          <textarea className="col-span-1 h-full border-2 border-gray-900 p-3 font-body" onChange={handleInput}>

          </textarea>
          <div className="col-span-1 grid grid-rows-4 gap-2">
            <div className="row-span-1 grid grid-cols-2">
              <div className="text-white col-span-1 p-8 font-body text-center">
                <div className="bg-black py-2 rounded-md cursor-pointer" onClick={getTokens}>
                  Lex
                </div>
              </div>
              <div className="text-gray-900 col-span-1 p-8 font-body text-center">
                <div className="bg-gray-200 py-2 rounded-md cursor-pointer" onClick={getColor}>
                  Parse
                </div>
              </div>
            </div>
            <div className="row-span-3 px-4">
              <div className="font-body text-center text-xl">Resultados</div>
              {(action=="parser") && <ParserResults text={parseObject.text} color={parseObject.color}/>}
              {(action=="lex") &&    <LexerResults lines={line_list} showModal={viewModal} setIndexTok={setIndexTok}/>}
              
              
            </div>
          </div>
        </div>
      </div>
      {showModal && <LexerResultsModal show={viewModal} token={index_token}/>}
    </div>
  );
}

export default App;
