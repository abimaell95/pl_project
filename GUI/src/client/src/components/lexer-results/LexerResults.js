import {LexerResultsTile} from '../../components';

//const list = [{line:"(def a 1)"},{line:"(+ 1 2)"},{line:"(+ 1 2)"},{line:"(+ 1 2)"},{line:"(+ 1 2)"}]

function LexerResults(props){
    return(
        <div className="flex flex-col h-64 overflow-auto">
            <div className="grid grid-cols-2">
                <div className="col-span-1 bg-gray-900 rounded-tl-md text-white text-center py-1">
                    Line
                </div>
                <div className="col-span-1 bg-gray-900 rounded-tr-md text-white text-center py-1">
                    Result
                </div>
            </div>
            {props.lines.map((line,idx)=>{
                return <LexerResultsTile line={line} showModal={props.showModal} setIndexTok={()=>{props.setIndexTok(idx)}}/>
            })}
        </div>
    )
}

export {LexerResults}