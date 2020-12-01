const list = [{char:"atom",token:"ATOM"},{char:"def",token:"DEF"},{char:"(",token:"PLEFT"},{char:"1",token:"NUMBER"},{char:"1",token:"NUMBER"},{char:"1",token:"NUMBER"},{char:"1",token:"NUMBER"},{char:"1",token:"NUMBER"},{char:"1",token:"NUMBER"},{char:"1",token:"NUMBER"},{char:"1",token:"NUMBER"},{char:"1",token:"NUMBER"},{char:"1",token:"NUMBER"}]
function LexerResultsModal(props){
    return(
        <>
            <div className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none">
                <div className="relative w-auto my-auto mx-auto max-w-md">
                    {/*content*/}
                    <div className="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
                        {/*header*/}
                        <div className="flex items-start justify-between p-3 border-b border-solid border-gray-300 rounded-t">
                            <h3 className="text-3xl font-normal font-body text-gray-900 mr-2">
                                Resultados
                            </h3>
                            <button className="p-1 ml-auto bg-transparent border-0 text-white opacity-5 float-right text-3xl leading-none font-semibold outline-none focus:outline-none">
                                <span className="bg-transparent text-gray-900 opacity-5 h-6 w-6 text-2xl block outline-none focus:outline-none">
                                    ×
                                </span>
                            </button>
                        </div>
                        {/*body*/}
                        <div className="my-4 mx-2">
                            <div className="flex flex-col overflow-auto h-96">
                                <div className="grid grid-cols-2">
                                    <div className="col-span-1 bg-gray-900 rounded-tl-md text-white text-center py-1">
                                        Char
                                    </div>
                                    <div className="col-span-1 bg-gray-900 rounded-tr-md text-white text-center py-1">
                                        Token
                                    </div>
                                </div>
                                {list.map((tok)=>{
                                    return(
                                        <div className="grid grid-cols-2">
                                            <div className="col-span-1 bg-gray-200 text-gray-900 text-center py-1 font-body">
                                                {tok.char}
                                            </div>
                                            <div className="col-span-1 bg-gray-200 text-gray-900 text-center py-1 font-body">
                                                {tok.token}
                                            </div>
                                        </div>
                                    )
                                })}
                            </div>
                        </div>
                        {/*footer*/}
                        <div className="flex items-center justify-end p-2 border-t border-solid border-gray-300 rounded-b">
                            <button
                                className="text-gray-500 background-transparent font-bold uppercase px-6 py-2 text-sm outline-none focus:outline-none mr-1 mb-1" 
                                type="button"
                                style={{ transition: "all .15s ease" }}
                            >
                                Cerrar
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            <div className="opacity-50 fixed inset-0 z-40 bg-black"></div>
        </>
    )
}

export {LexerResultsModal}