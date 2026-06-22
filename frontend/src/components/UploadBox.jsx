function UploadBox({

handleImage

}){

return(

<div className="uploadBox">

<input

type="file"

accept=".jpg,.jpeg,.png,.webp"

onChange={handleImage}

/>

</div>

)

}

export default UploadBox;