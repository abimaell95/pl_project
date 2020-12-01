import {ParserResults,LexerResults,LexerResultsModal} from './components';
function App() {

  return (
    <div className="App p-24">
      <div className="flex flex-col">
        <header className="font-body text-4xl text-center">
          LEXER & PARSER VALIDATOR
        </header>
        <div className="grid grid-cols-2 h-full mt-5 px-40 gap-2">
          <textarea className="col-span-1 h-full border-2 border-gray-900 p-3 font-body">

          </textarea>
          <div className="col-span-1 grid grid-rows-4 gap-2">
            <div className="row-span-1 grid grid-cols-2">
              <div className="text-white col-span-1 p-8 font-body text-center">
                <div className="bg-black py-2 rounded-md cursor-pointer">
                  Lex
                </div>
              </div>
              <div className="text-gray-900 col-span-1 p-8 font-body text-center">
                <div className="bg-gray-200 py-2 rounded-md cursor-pointer">
                  Parse
                </div>
              </div>
            </div>
            <div className="row-span-3 px-4">
              <div className="font-body text-center text-xl">Resultados</div>
              <ParserResults/>
              <LexerResults/>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
