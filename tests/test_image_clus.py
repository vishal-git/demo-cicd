import sys

sys.path.append("./src")
from image_clus import clus_images


class TestImageClustering:
    """
    Test class for Image Clustering
    """

    test_data_dir = "./data/*"
    expected_clusters = [[1, 0, 10], [5, 12, 7], [6, 9], [8, 11]]

    def test_cluster_assignments(self):
        """
        WHEN the test data is passed
        THEN appropriate (known) images should be in the same clusters
        """
        _, clusters = clus_images(self.test_data_dir)

        for cluster in clusters:
            matched = 0
            for expected_cluster in self.expected_clusters:
                if set(cluster) == set(expected_cluster):
                    matched = 1

            assert matched == 1, f"Some images are not in the expected cluster together"

    def test_cluster_number(self):
        """
        WHEN the test data is passed
        THEN exactly four clusters should be identified
        """
        _, clusters = clus_images(self.test_data_dir)

        assert len(clusters) == 4, f"Expected four clusters but got {len(clusters)}"

    def test_all_images_assigned(self):
        """
        WHEN the test data is passed
        THEN all images must be assigned to a cluster
        """
        n_images, clusters = clus_images(self.test_data_dir)

        images_w_clus_assignment = [i for cluster in clusters for i in cluster]

        assert (
            len(images_w_clus_assignment) == n_images
        ), f"Not all images are assigned to a cluster"
