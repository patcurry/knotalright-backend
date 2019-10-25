import { Router } from 'express';
import getBodyData from './getBodyData';

const router = Router();

router.get('/', async (req, res) => {
    const models = req.context.models;
    const knots = await models.Knot.findAll();
    return res.send(knots);
});

router.get('/:knotId', async (req, res) => {
    const models = req.context.models;
    const knot = await models.Knot.findByPk(
        req.params.knotId,
    );
    return res.send(knot);
});

router.post('/', async (req, res) => {
    const models = req.context.models;
    const body = req.body;
    const knot = await models.Knot.create(getBodyData(body));
    return res.send(knot);
});

router.put('/:knotId', async (req, res) => {
    const models = req.context.models;
    const body = req.body;
    const knotId = req.params.knotId;
    const knot = await models.Knot.findByPk(knotId)
        .then(knot => knot.update(getBodyData(body)));
    return res.send(knot);
});

router.delete('/:knotId', async (req, res) => {
    const models = req.context.models;
    const knotId = req.params.knotId;
    const knot = await models.Knot.findByPk(knotId)
        .then(knot => knot.destroy());
    return res.send('Knot deleted.');
});

export default router;
