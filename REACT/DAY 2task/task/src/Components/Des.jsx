import img from "../assets/virat.jpg"


export const Des = () => {
    let imag="https://cdn.siasat.com/wp-content/uploads/2026/03/peddi.jpg"
    return (
        <>
        <div className="parent">

            <div className="card1" style={{ width: "18rem" }}>

                <img
                    src={imag}
                    className="card-img-top"
                    alt="" height={280} width={280}
                    />

                <div className="card-body">

                    <h5 className="card-title">Coffee Cafe</h5>

                    <p className="card-text">
                        Some quick example text to build on the card title.
                    </p>

                    <a href="#" className="btn btn-primary">
                        Go somewhere
                    </a>

                </div>
            </div>
            <div className="card2" style={{ width: "18rem" }}>

                <img
                    src={img}
                    className="card-img-top"
                    alt="coffee"
                    height={280} width={280}
                    />

                <div className="card-body">

                    <h5 className="card-title">Coffee Cafe</h5>

                    <p className="card-text">
                        Some quick example text to build on the card title.
                    </p>

                    <a href="#" className="btn btn-primary">
                        Go somewhere
                    </a>

                </div>
            </div>
            <div className="card3" style={{ width: "18rem" }}>

                <img
                    src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxmiV_bDsadQvS1WypMs4TufmcKEcDhmkgNw&s"
                    className="card-img-top"
                    alt="coffee"
                    height={280} width={280}
                    />

                <div className="card-body">

                    <h5 className="card-title">Coffee Cafe</h5>

                    <p className="card-text">
                        Some quick example text to build on the card title.
                    </p>

                    <a href="#" className="btn btn-primary">
                        Go somewhere
                    </a>

                </div>
            </div>
        </div>
        </>
    )
}