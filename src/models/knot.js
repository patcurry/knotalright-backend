const knot = (sequelize, DataTypes) => {
    const Knot = sequelize.define('knot', {
        name: {
            type: DataTypes.STRING,
            unique: true,
        },
        description: DataTypes.TEXT,
    });
    return Knot;
};

export default knot;