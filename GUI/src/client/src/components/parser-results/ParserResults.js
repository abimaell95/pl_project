function ParserResults(props){

    return(
        <div className={`text-${props.color}-700 font-body text-xl`}>
            {props.text}
        </div>
    )
}

export {ParserResults}