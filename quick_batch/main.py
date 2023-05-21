import fire
from utilities import param_checks
from utilities import manage_images
from utilities import manage_containers


def main(config="",
         processor=""):

    # check that input files exist
    input_path, output_path = param_checks.check_files(config, processor)

    # create docker client
    client = manage_images.create_client()

    # build images
    manage_images.build_processor_image(client)
    manage_images.build_queue_image(client)
    manage_images.build_controller_image(client)

    # kill current containers
    manage_containers.remove_all_containers(client)

    # create network
    manage_containers.create_network(client)

    # startup queue container
    queue_container = manage_containers.\
        startup_queue_app(client, config, input_path)

    # startup processor container
    processor_container = manage_containers.\
        startup_processor_app(client, config, input_path, output_path)


if __name__ == '__main__':
    fire.Fire(main)
