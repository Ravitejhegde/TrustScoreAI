function ImagePreview({

image

}){

if(!image){

return null

}

return(

<img

src={URL.createObjectURL(image)}

alt="preview"

className="preview"

/>

)

}

export default ImagePreview;