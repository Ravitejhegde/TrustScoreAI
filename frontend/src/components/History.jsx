function History({

history

}){

if(

history.length===0

){

return null

}

return(

<div className="history">

<h2>

Analysis History

</h2>

{

history.map(

(item,index)=>(

<div

key={index}

className="historyCard"

>

<h3>

{item.name}

</h3>

<p>

Score: {item.score}

</p>

<p>

{item.risk}

</p>

<p>

{item.time}

</p>

</div>

)

)

}

</div>

)

}

export default History;