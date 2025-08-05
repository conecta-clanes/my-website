import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Material Auxiliar',
    Svg: require('@site/static/img/documents.svg').default,
    description: (
      <>
        Material sobre técnica y diversas actividades
      </>
    ),
  },
  {
    title: 'Formatos',
    Svg: require('@site/static/img/documents.svg').default,
    description: (
      <>
       Platillas
      </>
    ),
  },
  {
    title: 'Propuestas',
    Svg: require('@site/static/img/documents.svg').default,
    description: (
      <>
        Sobre lo que no esta documentado
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
