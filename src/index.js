// knotalright/src/index.js
import 'dotenv/config';
import cors from 'cors';
import bodyParser from 'body-parser';
import express from 'express';

import models, { sequelize } from './models';
import routes from './routes';

const app = express();

// Application-Level Middleware
app.use(cors());

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// not sure why I need this
app.use(async (req, res, next) => {
    req.context = {
        models,
    };
    next();
});

app.use('/knots', routes.knot);

// Start
const eraseDatabaseOnSync = true;

sequelize.sync({ force: eraseDatabaseOnSync }).then(async () => {
    if (eraseDatabaseOnSync) {
        createKnots();
    }

    app.listen(process.env.PORT, () =>
        console.log(`Example app listening on port ${process.env.PORT}!`),
    );
});

// seed the database with knots
const createKnots = async () => {
    await models.Knot.create({
        name: 'Figure Eight Follow Through',
        description: 'Tie a figure eight, then loop through something and follow it back through.',
    });
};
