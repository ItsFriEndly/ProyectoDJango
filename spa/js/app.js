const { createApp } = Vue;

const formatearPrecio = (precio) =>
    precio.toLocaleString('es-ES', { style: 'currency', currency: 'EUR' });

const Inicio = {
    props: ['datos'],
    template: `
        <section class="portada">
            <h2>¿Qué es el comercio justo?</h2>
            <p>
                El comercio justo es un sistema comercial basado en el diálogo, la transparencia y el respeto,
                que busca una mayor equidad en el comercio internacional y mejores condiciones para los
                productores y trabajadores.
            </p>
            <div class="resumen">
                <a href="#/productos" class="tarjeta resumen-item">
                    <span class="cifra">{{ datos.productos.length }}</span> productos
                </a>
                <a href="#/categorias" class="tarjeta resumen-item">
                    <span class="cifra">{{ datos.categorias.length }}</span> categorías
                </a>
                <a href="#/certificaciones" class="tarjeta resumen-item">
                    <span class="cifra">{{ datos.certificaciones.length }}</span> certificaciones
                </a>
            </div>
            <h2>Productos destacados</h2>
            <div class="rejilla">
                <tarjeta-producto v-for="p in destacados" :key="p.id" :producto="p" :datos="datos"></tarjeta-producto>
            </div>
        </section>
    `,
    computed: {
        destacados() {
            return [...this.datos.productos]
                .sort((a, b) => b.certificaciones.length - a.certificaciones.length)
                .slice(0, 3);
        },
    },
};

const Productos = {
    props: ['datos', 'categoria', 'certificacion'],
    data() {
        return {
            busqueda: '',
            categoriaSeleccionada: this.categoria || '',
            certificacionSeleccionada: this.certificacion || '',
            orden: 'nombre',
        };
    },
    template: `
        <section>
            <h2>Productos</h2>
            <div class="filtros">
                <input v-model.trim="busqueda" type="search" placeholder="Buscar por nombre o descripción..." aria-label="Buscar">
                <select v-model="categoriaSeleccionada" aria-label="Categoría">
                    <option value="">Todas las categorías</option>
                    <option v-for="c in datos.categorias" :key="c.id" :value="String(c.id)">{{ c.nombre }}</option>
                </select>
                <select v-model="certificacionSeleccionada" aria-label="Certificación">
                    <option value="">Todas las certificaciones</option>
                    <option v-for="c in datos.certificaciones" :key="c.id" :value="String(c.id)">{{ c.nombre }}</option>
                </select>
                <select v-model="orden" aria-label="Ordenar">
                    <option value="nombre">Ordenar por nombre</option>
                    <option value="precio-asc">Precio: menor a mayor</option>
                    <option value="precio-desc">Precio: mayor a menor</option>
                </select>
                <button v-if="hayFiltros" type="button" class="boton-secundario" @click="limpiar">Limpiar filtros</button>
            </div>
            <p class="contador">{{ filtrados.length }} de {{ datos.productos.length }} productos</p>
            <transition-group name="lista" tag="div" class="rejilla">
                <tarjeta-producto v-for="p in filtrados" :key="p.id" :producto="p" :datos="datos"></tarjeta-producto>
            </transition-group>
            <p v-if="!filtrados.length" class="aviso">No se ha encontrado ningún producto.</p>
        </section>
    `,
    computed: {
        hayFiltros() {
            return this.busqueda || this.categoriaSeleccionada || this.certificacionSeleccionada;
        },
        filtrados() {
            const texto = this.busqueda.toLowerCase();
            const resultado = this.datos.productos.filter((p) =>
                (!texto || p.nombre.toLowerCase().includes(texto) || p.descripcion.toLowerCase().includes(texto)) &&
                (!this.categoriaSeleccionada || p.categoria === Number(this.categoriaSeleccionada)) &&
                (!this.certificacionSeleccionada || p.certificaciones.includes(Number(this.certificacionSeleccionada)))
            );
            const comparadores = {
                'nombre': (a, b) => a.nombre.localeCompare(b.nombre, 'es'),
                'precio-asc': (a, b) => a.precio - b.precio,
                'precio-desc': (a, b) => b.precio - a.precio,
            };
            return resultado.sort(comparadores[this.orden]);
        },
    },
    methods: {
        limpiar() {
            this.busqueda = '';
            this.categoriaSeleccionada = '';
            this.certificacionSeleccionada = '';
        },
    },
};

const ProductoDetalle = {
    props: ['datos', 'id'],
    template: `
        <section v-if="producto" class="detalle">
            <a href="#/productos" class="volver">&larr; Volver a productos</a>
            <h2>{{ producto.nombre }}</h2>
            <p class="precio grande">{{ precio }}</p>
            <p>{{ producto.descripcion }}</p>
            <p>
                <strong>Categoría:</strong>
                <a :href="'#/productos?categoria=' + categoria.id">{{ categoria.nombre }}</a>
            </p>
            <div>
                <strong>Certificaciones:</strong>
                <ul v-if="certificaciones.length" class="etiquetas">
                    <li v-for="c in certificaciones" :key="c.id">
                        <a :href="'#/productos?certificacion=' + c.id" class="etiqueta" :title="c.descripcion">{{ c.nombre }}</a>
                    </li>
                </ul>
                <span v-else> ninguna</span>
            </div>
        </section>
        <no-encontrado v-else></no-encontrado>
    `,
    computed: {
        producto() {
            return this.datos.productos.find((p) => p.id === Number(this.id));
        },
        categoria() {
            return this.datos.categoriasPorId[this.producto.categoria];
        },
        certificaciones() {
            return this.producto.certificaciones.map((id) => this.datos.certificacionesPorId[id]);
        },
        precio() {
            return formatearPrecio(this.producto.precio);
        },
    },
};

const Categorias = {
    props: ['datos'],
    template: `
        <section>
            <h2>Categorías</h2>
            <div class="rejilla">
                <a v-for="c in datos.categorias" :key="c.id" :href="'#/productos?categoria=' + c.id" class="tarjeta">
                    <h3>{{ c.nombre }}</h3>
                    <p>{{ c.descripcion }}</p>
                    <p class="contador">{{ numProductos(c.id) }} productos &rarr;</p>
                </a>
            </div>
        </section>
    `,
    methods: {
        numProductos(id) {
            return this.datos.productos.filter((p) => p.categoria === id).length;
        },
    },
};

const Certificaciones = {
    props: ['datos'],
    data() {
        return { abierta: null };
    },
    template: `
        <section>
            <h2>Certificaciones</h2>
            <div class="acordeon">
                <div v-for="c in datos.certificaciones" :key="c.id" class="tarjeta">
                    <button type="button" class="acordeon-titulo" @click="abierta = abierta === c.id ? null : c.id" :aria-expanded="abierta === c.id">
                        {{ c.nombre }}
                        <span>{{ abierta === c.id ? '−' : '+' }}</span>
                    </button>
                    <transition name="fundido">
                        <div v-if="abierta === c.id">
                            <p>{{ c.descripcion }}</p>
                            <a :href="'#/productos?certificacion=' + c.id">Ver los {{ numProductos(c.id) }} productos certificados &rarr;</a>
                        </div>
                    </transition>
                </div>
            </div>
        </section>
    `,
    methods: {
        numProductos(id) {
            return this.datos.productos.filter((p) => p.certificaciones.includes(id)).length;
        },
    },
};

const NoEncontrado = {
    template: `
        <section class="aviso">
            <h2>Página no encontrada</h2>
            <a href="#/">Volver al inicio</a>
        </section>
    `,
};

const TarjetaProducto = {
    props: ['producto', 'datos'],
    template: `
        <a :href="'#/productos/' + producto.id" class="tarjeta">
            <span class="categoria">{{ datos.categoriasPorId[producto.categoria].nombre }}</span>
            <h3>{{ producto.nombre }}</h3>
            <p class="precio">{{ precio }}</p>
            <p v-if="producto.certificaciones.length" class="contador">
                {{ producto.certificaciones.length }} {{ producto.certificaciones.length > 1 ? 'certificaciones' : 'certificación' }}
            </p>
        </a>
    `,
    computed: {
        precio() {
            return formatearPrecio(this.producto.precio);
        },
    },
};

function resolverRuta(hash) {
    const [ruta, consulta = ''] = hash.replace(/^#/, '').split('?');
    const parametros = Object.fromEntries(new URLSearchParams(consulta));
    const partes = ruta.split('/').filter(Boolean);

    if (partes.length === 0) return { componente: 'Inicio', props: {} };
    if (partes[0] === 'productos' && partes.length === 1) return { componente: 'Productos', props: parametros };
    if (partes[0] === 'productos' && partes.length === 2) return { componente: 'ProductoDetalle', props: { id: partes[1] } };
    if (partes[0] === 'categorias' && partes.length === 1) return { componente: 'Categorias', props: {} };
    if (partes[0] === 'certificaciones' && partes.length === 1) return { componente: 'Certificaciones', props: {} };
    return { componente: 'NoEncontrado', props: {} };
}

const app = createApp({
    data() {
        return {
            rutaActual: window.location.hash,
            datos: null,
            cargando: true,
            error: null,
            versionVue: Vue.version,
            enlaces: [
                { ruta: '/', texto: 'Inicio' },
                { ruta: '/productos', texto: 'Productos' },
                { ruta: '/categorias', texto: 'Categorías' },
                { ruta: '/certificaciones', texto: 'Certificaciones' },
            ],
        };
    },
    computed: {
        vista() {
            return resolverRuta(this.rutaActual);
        },
        seccionActiva() {
            const primera = this.rutaActual.replace(/^#/, '').split(/[/?]/).filter(Boolean)[0];
            return primera ? '/' + primera : '/';
        },
    },
    async mounted() {
        window.addEventListener('hashchange', () => {
            this.rutaActual = window.location.hash;
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
        try {
            const respuesta = await fetch('data/datos.json');
            if (!respuesta.ok) throw new Error(`HTTP ${respuesta.status}`);
            const datos = await respuesta.json();
            datos.categoriasPorId = Object.fromEntries(datos.categorias.map((c) => [c.id, c]));
            datos.certificacionesPorId = Object.fromEntries(datos.certificaciones.map((c) => [c.id, c]));
            this.datos = datos;
        } catch (e) {
            this.error = e.message;
        } finally {
            this.cargando = false;
        }
    },
});

app.component('Inicio', Inicio);
app.component('Productos', Productos);
app.component('ProductoDetalle', ProductoDetalle);
app.component('Categorias', Categorias);
app.component('Certificaciones', Certificaciones);
app.component('NoEncontrado', NoEncontrado);
app.component('TarjetaProducto', TarjetaProducto);
app.mount('#app');
