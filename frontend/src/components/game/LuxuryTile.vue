<template>
    <div class="tile" :class="hiLight(value, points, luxuryTiles[selectedLuxuryTile])">
         {{points}} ${{value}}
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';

    export default {
        props: ['value','points'],
        computed: {
            ...mapGetters([
                'luxuryTiles',
                'selectedLuxuryTile'
            ])    
        },
        methods: {
            hiLight(value,points, sel) {
                if (sel && sel.value==value && sel.points== points) {
                    return "hilight";
                } else {
                    return "nohilight";
                }
            }
        }
    }    
</script>

<style scoped>

.tile {
    background-color: darkblue;
    font-size: 1.2em;
    font-weight: bold;
    text-align: center;
    text-shadow: -1px 0 white, 0 1px white, 1px 0 white, 0 -1px white;
    width: 70px;
}

.hilight {
    box-shadow: 4px 4px 4px grey;
}

.nohilight {
}

</style>
