import {Table} from 'phosphor-react'
function LexerResultsTile(props){
    return(
        <div className="grid grid-cols-2">
            <div className="flex items-center justify-center col-span-1 bg-gray-200 text-gray-900 text-center font-body py-2">
                <div className="">
                    {props.line}
                </div>
            </div>
            <div className="col-span-1 bg-gray-200 text-gray-900 text-center py-4 px-16">
                <div className="flex items-center justify-center bg-black text-white rounded-md cursor-pointer py-1">
                    <div className="">
                        <Table size={24} color="#fcfcfc"/>
                    </div> 
                </div>
            </div>
        </div>
    )
}

export {LexerResultsTile}