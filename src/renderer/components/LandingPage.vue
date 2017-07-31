<template>
  <div id="wrapper">
    <button @click="onClick"
            class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
      Button
    </button>
    <img class="fpv-image" :src="image">
    <!--img id="logo" style="width: 100px" src="~@/assets/logo.png" alt="electron-vue"-->
  </div>
</template>

<script>
  import protobuf from 'protobufjs'

  let FpvImage

  export default {
    data () {
      return {
        image: null
      }
    },

    methods: {
      concatTypedArrays (a, b) { // a, b TypedArray of same type
        let c = new (a.constructor)(a.length + b.length)
        c.set(a, 0)
        c.set(b, a.length)
        return c
      },

      pump (reader, chunks, callback) {
        return reader.read().then((result) => {
          if (result.value) {
            if (chunks) {
              chunks = this.concatTypedArrays(chunks, result.value)
            } else {
              chunks = result.value
            }
            // chunks.push(result.value)
          }

          if (result.done) {
            callback(chunks)
          } else {
            return this.pump(reader, chunks, callback)
          }
        }).catch((e) => {
          console.log(e)
        })
      },

      pumpPromise (reader) {
        let chunks = null // []
        return new Promise((resolve) => {
          this.pump(reader, chunks, (chunks) => {
            resolve(chunks)
          })
        })
      },

      onClick () {
        fetch('http://localhost:9999')
          .then((response) => {
            return this.pumpPromise(response.body.getReader())
          })
          .then((binaryData) => {
            let message = FpvImage.decode(binaryData)
            let base64Data = btoa(String.fromCharCode.apply(null, message.image))
            // console.log(message, base64Data)
            this.image = 'data:image/png;base64,' + base64Data
          })
      },

      open (link) {
        this.$electron.shell.openExternal(link)
      }
    },
    created () {
      protobuf.load('static/fpv_image.proto', (err, root) => {
        if (err) {
          console.log(err)
        }

        FpvImage = root.lookupType('hapt.FpvImage')

//        setInterval(() => {
//          this.onClick()
//        }, 150)
        // console.log(FpvImage)
      })
    }
  }
</script>

<style lang="scss">
  .fpv-image {
    width: 400px;
    height: 300px;
    background: #555;
  }
</style>
