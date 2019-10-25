// This is a helper function to get the data from the body and
// put it into the right form for sequelize to create
// or update a model
export default dict => {
    const bodyData = {};
    Object.keys(dict)
        .map(attribute => {
            bodyData[attribute] = dict[attribute]
        });
    return bodyData;
}