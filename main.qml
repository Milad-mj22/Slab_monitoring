import QtQuick 2.14
import QtQuick.Window 2.14
import QtMultimedia 5.14

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    GridView {
        width: 300; height: 200

        model: manager !== null ? manager.services : []
        delegate: VideoOutput {
            width: 100
            height: 100
            fillMode: VideoOutput.PreserveAspectCrop
            source: model.modelData
        }
    }
}